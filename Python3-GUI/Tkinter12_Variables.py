# coding=utf-8
import tkinter as tk

win = tk.Tk()

strData = tk.StringVar()  # Assign tkinter Variable to strData variable
print(type(strData), strData)
strData.set('Hello StringVar')  # Set strData variable
varData = strData.get()  # Get value of strData variable
print(type(varData), varData)

intData = tk.IntVar()
print(type(intData), intData)
intData.set(111)
add_int = intData.get() + 222
print(type(add_int), add_int)

doubleData = tk.DoubleVar()
print(type(doubleData), doubleData)
doubleData.set(1.1234567890)
add_doubles = 2.00000000001234567890 + doubleData.get()
print(type(add_doubles), add_doubles)

# the default tkinter variable values
print("StringVar:{} - IntVar:{} - DoubleVar:{} - BooleanVar:{}".format(tk.StringVar().get(),
                                                                       tk.IntVar().get(),
                                                                       tk.DoubleVar().get(),
                                                                       tk.BooleanVar().get()))
