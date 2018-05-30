# -*- coding: utf-8 -*-
import tkinter
from tkinter.constants import *

tk = tkinter.Tk()
tk.wm_title("Tkinter01 Demo")
frame = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)
frame.pack(fill=BOTH, expand=1)
label = tkinter.Label(frame, text="Hello, World")
label.pack(fill=X, expand=1)
button = tkinter.Button(frame, text="Exit", command=tk.destroy)
button.pack(side=BOTTOM)
tk.mainloop()

# ### Tkinter
# https://docs.python.org/3/library/tk.html
# Python内置的支持Tk的图形模块，简单方便，能够满足基本的GUI程序要求；
# 虽然tkinter的界面简陋，但其简洁的优点，适合用于小工具、示例程序、Demo等快速开发场景；
# 编写GUI程序的一般过程：创建窗口---》添加组件并设置属性---》绑定事件响应；
# 源码__init__.py文件包含常用的绝大多数类（“Python安装目录\Lib\tkinter\__init__.py”）；
#
# ### 组件（widget）
# 也称为控件，包括标签、按钮、菜单、对话框、消息框等；
# 每个组件都有相应的类，可以通过面向对象的方式去使用；
# 某些组件的方法是共用的，方法名相同，属性设置也相同；
#
# ### 常量（constants）
# 具体信息可查看源码文件（“Python安装目录\Lib\tkinter\constants.py”）；
