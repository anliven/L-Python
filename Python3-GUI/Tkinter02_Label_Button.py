# coding=utf-8
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

a_label = ttk.Label(win, text="A Label")  # Adding a Label
a_label.grid(column=0, row=0)


# Button Click Event Function
def click_me():
    action.configure(text="** I have been Clicked! **")
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')


# Adding a Button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1, row=0)
# action.configure(state='disabled')  # Disable the Button Widget

win.mainloop()
