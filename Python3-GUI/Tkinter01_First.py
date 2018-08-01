# coding=utf-8
import tkinter as tk

win = tk.Tk()  # Create instance
win.title("Python GUI")  # Add a title
win.iconbitmap('Temp.ico')  # Change the main windows icon
win.resizable(False, False)  # Disable resizing the GUI by passing in False/False
# win.resizable(True, False)  # Enable resizing x-dimension, disable y-dimension

win.mainloop()  # Start GUI
