import tkinter as tk

def onClick():
    x = entry1.get()

baseWindow = tk.Tk()
baseWindow.title("Simple program")
baseWindow.geometry("1920x1080")

label1 = tk.Label(baseWindow, text = "Хуй", fg = "#FF5561", font = "Arial 30")
label1.pack(side="top")

entry1 = tk.Entry(baseWindow, fg = "#FF5561", bg = "white", font="Arial 18")
entry1.pack(side="top")

click = tk.Button(baseWindow, text="Взять в рот", font = "Arial 18", command=onClick())
click.pack()


baseWindow.mainloop()