import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

questions = []
current_question_index = 0
score = 0
selected_answers_vars = []
test_results = []

root = tk.Tk()
root.title("Тестовая система")
root.geometry("600x400")

question_label = tk.Label(root, text="", font=("Arial", 12, "bold"), wraplength=550, justify="left")
question_label.pack(pady=20)

answers_frame = tk.Frame(root)
answers_frame.pack(pady=10, fill="both", expand=True)

status_label = tk.Label(root, text="", font=("Arial", 10))
status_label.pack(pady=5)

answer_button = tk.Button(root, text="Ответить", font=("Arial", 12), bg="lightblue", padx=20)
answer_button.pack(pady=10)

def load_questions():
    global questions
    try:
        with open("test_questions.txt", "r", encoding="utf-8") as file:
            content = file.read().strip()
        
        question_blocks = content.split('q:')[1:]
        
        for block in question_blocks:
            lines = block.strip().split('\n')
            question_text = lines[0].strip()
            
            answers = []
            correct_answers = []
            
            for line in lines[1:]:
                if line.strip() and line[0].isdigit():
                    answer_text = line[2:].strip()
                    
                    if answer_text.endswith('+'):
                        answer_text = answer_text[:-1].strip()
                        correct_answers.append(answer_text)
                    
                    answers.append(answer_text)
            
            questions.append({
                'question': question_text,
                'answers': answers,
                'correct': correct_answers
            })
            
    except FileNotFoundError:
        messagebox.showerror("Ошибка", "Файл test_questions.txt не найден!")
        root.destroy()

def save_results_to_json():
    global test_results
    
    result_data = {
        "test_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_questions": len(questions),
        "correct_answers": score,
        "percentage": round((score / len(questions)) * 100, 1),
        "questions": test_results
    }
    
    try:
        try:
            with open("test_results.json", "r", encoding="utf-8") as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = {"test_sessions": []}
        
        existing_data["test_sessions"].append(result_data)
        
        with open("test_results.json", "w", encoding="utf-8") as f:
            json.dump(existing_data, f, ensure_ascii=False, indent=2)
        
    except Exception as e:
        messagebox.showerror("Ошибка", f"Не удалось сохранить результаты: {str(e)}")

def show_question():
    global selected_answers_vars, current_question_index
    
    for widget in answers_frame.winfo_children():
        widget.destroy()
    
    selected_answers_vars = []
    
    if current_question_index < len(questions):
        question_data = questions[current_question_index]
        
        question_label.config(
            text=f"Вопрос {current_question_index + 1}/{len(questions)}:\n{question_data['question']}"
        )
        
        for i, answer in enumerate(question_data['answers']):
            var = tk.BooleanVar()
            selected_answers_vars.append(var)
            
            cb = tk.Checkbutton(
                answers_frame,
                text=answer,
                variable=var,
                font=("Arial", 10),
                wraplength=500,
                justify="left"
            )
            cb.pack(anchor="w", pady=2)
        
        status_label.config(
            text=f"Вопрос {current_question_index + 1} из {len(questions)}"
        )
    else:
        show_results()

def check_answer():
    global current_question_index, score, test_results
    
    if current_question_index >= len(questions):
        return
    
    question_data = questions[current_question_index]
    user_selected = []
    
    for i, var in enumerate(selected_answers_vars):
        if var.get():
            user_selected.append(question_data['answers'][i])
    
    is_correct = set(user_selected) == set(question_data['correct'])
    
    if is_correct:
        score += 1
    
    test_results.append({
        "question_number": current_question_index + 1,
        "question": question_data['question'],
        "user_answers": user_selected,
        "correct_answers": question_data['correct'],
        "is_correct": is_correct
    })
    
    current_question_index += 1
    show_question()

def show_results():
    for widget in root.winfo_children():
        widget.destroy()
    
    total_questions = len(questions)
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0
    
    result_text = f"Тест завершен!\n\n"
    result_text += f"Правильных ответов: {score} из {total_questions}\n"
    result_text += f"Процент правильных ответов: {percentage:.1f}%\n\n"
    
    if percentage >= 80:
        result_text += "Отличный результат!"
    elif percentage >= 60:
        result_text += "Хороший результат!"
    else:
        result_text += "Попробуйте еще раз!"
    
    result_label = tk.Label(root, text=result_text, font=("Arial", 14, "bold"), justify="center")
    result_label.pack(expand=True, pady=20)
    
    save_results_to_json()
    
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)
    
    show_details_button = tk.Button(button_frame, text="Показать детали", command=show_details, font=("Arial", 10), bg="lightgreen", padx=15)
    show_details_button.pack(side="left", padx=10)
    
    exit_button = tk.Button(button_frame, text="Выход", command=root.quit, font=("Arial", 10), bg="lightcoral", padx=15)
    exit_button.pack(side="left", padx=10)

def show_details():
    details_window = tk.Toplevel(root)
    details_window.title("Детали теста")
    details_window.geometry("700x500")
    
    text_widget = tk.Text(details_window, wrap="word", font=("Arial", 10))
    text_widget.pack(fill="both", expand=True, padx=10, pady=10)
    
    details_text = "ДЕТАЛИ ТЕСТА:\n" + "="*50 + "\n\n"
    
    for i, result in enumerate(test_results):
        details_text += f"Вопрос {i+1}: {result['question']}\n"
        details_text += f"Ваш ответ: {', '.join(result['user_answers']) or 'Нет ответа'}\n"
        details_text += f"Правильный ответ: {', '.join(result['correct_answers'])}\n"
        details_text += f"Результат: {'Правильно' if result['is_correct'] else 'Неправильно'}\n"
        details_text += "-" * 50 + "\n\n"
    
    text_widget.insert("1.0", details_text)
    text_widget.config(state="disabled")
    
    close_button = tk.Button(details_window,text="Закрыть", command=details_window.destroy, font=("Arial", 10))
    close_button.pack(pady=10)

answer_button.config(command=check_answer)

load_questions()
show_question()

root.mainloop()