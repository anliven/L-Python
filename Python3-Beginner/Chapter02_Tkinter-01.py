#! python3
# -*- coding: utf-8 -*-
import tkinter
from turtle import Turtle

root = tkinter.Tk()  # 生成主窗口

menu = tkinter.Menu(root)  # 生成菜单
sub_menu = tkinter.Menu(menu, tearoff=0)  # 生成下拉菜单
sub_menu.add_command(label="Open")  # 在下拉菜单添加指令
sub_menu.add_command(label="Save")
menu.add_cascade(label="File", menu=sub_menu)  # 将下拉菜单添加到菜单
root.config(menu=sub_menu)

label = tkinter.Label(root, text="你好")  # 生成标签
label.pack()  # 将标签添加至主窗口
button1 = tkinter.Button(root, text="五角星")  # 生成按钮
button1.pack()  # 将按钮添加至主窗口


def star(event):  # 事件响应函数
    t = Turtle()
    for i in range(5):
        t.forward(100)
        t.right(144)


button1.bind('<Button-1>', star)  # 绑定事件
root.mainloop()  # 进入消息循环

# ### Tkinter
# Python内置的支持Tk的图形模块，无需安装任何包，可以直接使用，能够满足基本的GUI程序的要求；
# 如果是非常复杂的GUI程序，建议用操作系统原生支持的语言和库来编写；
# 编写GUI程序的一般过程：创建窗口---》添加组件---》事件响应；
# 常见的第三方图形界面库包括Tk、wxWidgets、Qt、GTK等；
