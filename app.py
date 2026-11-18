import tkinter as tk
from tkinter import *
from tkinter import ttk
from pathlib import Path
window = Tk()
window.title("Планировщик задач")
window.geometry("460x520")
logo = PhotoImage(file=str(Path(__file__).with_name("logo.png")))
picture = Label(image=logo)
picture.pack(pady=10)

label1 = Label(text="Название задачи")
label1.pack(anchor=W, padx=20, pady=1)
entry1 = ttk.Entry()
entry1.pack(fill=X, padx=20, pady=8)

label2 = Label(text="Длительность (дней)")
label2.pack(anchor=W, padx=20, pady=1)
entry2 = ttk.Entry()
entry2.pack(fill=X, padx=20, pady=8)

buttons_frame = Frame(window)
buttons_frame.pack(pady=5)

btn1 = Button(buttons_frame, text="Добавить задачу", bg="#12AF1A", fg="white", width=28)
btn1.pack()

btn = Button(buttons_frame, text="Очистить поля", width=28)
btn.pack()
counter = tk.Label(window, text="Задач добавлено: 0")
counter.pack(anchor=W, padx=20, pady=8)
window.mainloop()