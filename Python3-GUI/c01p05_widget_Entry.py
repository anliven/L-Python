# coding=utf-8
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)


def click_me():
    action.configure(text='Hello ' + name.get())


# Adding a Text box Entry widget
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()  # Place cursor into name Entry

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=1)

win.mainloop()
