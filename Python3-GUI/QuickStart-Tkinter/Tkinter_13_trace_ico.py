# -*- coding: utf-8 -*-
import tkinter as tk
from tkinter import ttk


def click_btn():  # Modified Button Click Function
    test_btn.configure(text='Hello')
    test_btn.configure(state='disabled')  # Disable the Button Widget


win = tk.Tk()
win.title("Tkinter13 Demo")
win.resizable(0, 0)
win.minsize(250, 100)
win.iconbitmap(r'Tkinter_13.ico')  # set ico

test_label = ttk.Label(win, text="Action is the antidote to despair!", width=30)
test_btn = tk.Button(win, text="点击失效", width=10, command=click_btn)

var_test = tk.StringVar()
var_test.set("hello tkinter")  # set the value of var
var_test.trace('w', print("# var_test:", var_test.get()))  # 跟踪变量var，当被重设时运行指定方法

var_dis = tk.IntVar()
var_un = tk.IntVar()
var_en = tk.IntVar()
check_btn1 = tk.Checkbutton(win, text="失效选项", variable=var_dis, state='disabled')
check_btn1.select()
check_btn2 = tk.Checkbutton(win, text="坚持", variable=var_un)
check_btn2.deselect()
check_btn3 = tk.Checkbutton(win, text="屈从", variable=var_en)
check_btn3.deselect()

test_label.pack(side="top", expand="yes", anchor="center")
test_btn.pack(side="bottom", expand="yes", anchor="center")
check_btn1.pack(side="bottom", expand="yes", anchor="center")
check_btn2.pack(side="bottom", expand="yes", anchor="center")
check_btn3.pack(side="bottom", expand="yes", anchor="center")


def checkCallback():  # only enable one checkbutton
    if var_un.get():
        check_btn3.configure(state='disabled')
    else:
        check_btn3.configure(state='normal')
    if var_en.get():
        check_btn2.configure(state='disabled')
    else:
        check_btn2.configure(state='normal')


var_un.trace('w', lambda unused0, unused1, unused2: checkCallback())
var_en.trace('w', lambda unused0, unused1, unused2: checkCallback())

win.mainloop()

# ### ico图标
# 通过iconbitmap()方法可设置GUI程序的图标；
#
# ### 变量及变量追踪
# StringVar是属于Tkinter下的对象，并不是python内建的对象；
# 此外还包括BooleanVar、DoubleVar、IntVar等；
# 使用StringVar等对象，不仅可以设置变量的值，而且可以跟踪变量值的变化；
# 常用方法：
# - set()：设置变量的值
# - get()：返回变量的值；
# - trace(mode, callback)：在指定mode（'w'--重设、'r'--读取）下触发时，调用callback函数；
