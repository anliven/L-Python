# coding=utf-8
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

ttk.Label(win, text="A Label").grid(column=0, row=0)  # Adding a Label

win.mainloop()
