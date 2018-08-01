# coding=utf-8
from tkinter import messagebox as msg
from tkinter import Tk

root = Tk()
root.withdraw()  # withdraw() function removes the debug window
msg.showinfo('This is a Title', 'Message Info Box:\nTest!')

# independent messagebox in one window
