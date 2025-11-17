import tkinter as tk
from tkinter import messagebox
import json
from datetime import datetime

root = tk.Tk()
root.title("Анкета о играх")
root.geometry("400x400")

answers = {}

def save_answers():
    answers["timestamp"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    answers["favorite_genre"] = genre.get()
    answers["play_frequency"] = frequency.get()
    answers["rating"] = rating.get()
    
    with open("answers.json", "a", encoding="utf-8") as f:
        json.dump(answers, f, ensure_ascii=False)
        f.write("\n")
    
    messagebox.showinfo("Спасибо!", "Ответы сохранены!")
    genre.delete(0, tk.END)
    frequency.delete(0, tk.END)
    rating.set(5)


tk.Label(root, text="Анкета о игровых предпочтениях", font=("Arial", 14, "bold")).pack(pady=20)

tk.Label(root, text="1. Любимый жанр игр:", font=("Arial", 11)).pack(pady=5)
genre = tk.Entry(root, font=("Arial", 11), width=30)
genre.pack(pady=5)

tk.Label(root, text="2. Как часто играете?", font=("Arial", 11)).pack(pady=10)
frequency = tk.Entry(root, font=("Arial", 11), width=30)
frequency.pack(pady=5)

tk.Label(root, text="3. Оценка игр как хобби (1-10):", font=("Arial", 11)).pack(pady=10)
rating = tk.Scale(root, from_=1, to=10, orient="horizontal", length=300, font=("Arial", 10))
rating.set(5)
rating.pack(pady=5)

tk.Button(root, text="Отправить ответы", command=save_answers, font=("Arial", 12, "bold"), bg="lightblue", padx=20, pady=10).pack(pady=20)

root.mainloop()