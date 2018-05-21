#! python3
# -*- coding: utf-8 -*-
import tkinter

root = tkinter.Tk()  # 创建根窗口
root.minsize(300, 100)
root.wm_title("Tkinter01 Demo")  # 修改窗口标题

label1 = tkinter.Label(root, text="This is a label!")  # 在指定窗口创建标签
label1.pack()  # Label的pack方法，调整自身尺寸和位置
label2 = tkinter.Label(root, text="This is a label!", font="12", background="blue")
label2.pack()
label3 = tkinter.Label(root, bitmap="warning")
label3.pack()


def onBtn1():
    in_label = tkinter.Label(root, text="Pressed")
    in_label.pack()


def onBtn2(event):  # bind()调用的函数必须接受一个参数表示该事件，如果不接受任何参数，则会报错
    in_label = tkinter.Label(root, text="Clicked")
    in_label.pack()


btn1 = tkinter.Button(root, text="Button One", command=onBtn1)  # command属性绑定事件
btn1.pack()
btn2 = tkinter.Button(root, text="Button Two")
btn2.bind("<Button-1>", onBtn2)  # bind()方法绑定事件，<Button-1>表示鼠标左键单击
btn2["width"] = 10  # 设置属性
btn2["height"] = 2
btn2["background"] = "red"
btn2.pack()

root.mainloop()  # 开始事件循环

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
# ### 标签（Label）
# 用来显示文本、图标、图像等信息，本身不执行任何功能；
# 标准属性包括background、font、bitmap、text、underline等；
#
# ### 按钮（Button）
# 用来执行相应的功能；
# 绑定事件的方式：在按钮组件被声明时用command属性绑定，或者使用bind()方法；
#
# ### 事件（event）
# bind()
# - 调用规则：窗体对象.bind(事件类型, 回调函数)；
# - “回调函数”:一般是自定义函数，当相应的事件发生时，自动调用；
# - 可以被绝大多数组件类使用，也就是说任何组件其实都可以模拟出button的效果；
# bind_all()
# - 用于全程序级别的绑定，通常用于全局的快捷键，比如F1打开帮助文档；
# - 参数类型与bind()相同；
# bind_class()
# - 可以绑定某些类；
# - 接受三个参数，第一个参数是类名，第二个参数是事件类型，第三个参数是相应的操作；
# unbind()
# - 解除绑定；
# - 只需要指定事件类型，将会解除该绑定事件类型的所有回调函数；
#
# ### 常用事件
# - <Button-1>  鼠标左键单击
# - <Button-2>  鼠标中键单击
# - <Button-3>  鼠标右键单击
# - <KeyPress-A>  表示A键被按下，其中的A可以换成其他键位
# - <Control-V>  表示按下的是Ctrl和V键，其中的V可以换成其他键位
# - <F1>  表示按下的是F1键，类似的，可以替换为F2等其他Fn系列键位
