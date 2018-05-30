# -*- coding: utf-8 -*-
import tkinter

root = tkinter.Tk()  # 创建根窗口
root.minsize(300, 100)
root.wm_title("Tkinter02 Demo")  # 修改窗口标题
root.resizable(width=True, height=False)  # 设置窗口尺寸是否可变，默认为True可变；

label1 = tkinter.Label(root, text="label One!")  # 在指定窗口创建标签
label1.pack()  # Label的pack方法，调整自身尺寸和位置
label2 = tkinter.Label(root, text="label Two!", font=("Arial", 12), bg="blue", width=12, height=2, bd=5)
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

# ### 标签（Label）
# 用来显示文本、图标、图像等信息，本身不执行任何功能；
# 标准属性包括background、font、bitmap、text、underline等；
# - text：显示的文本
# - bg或background: 背景颜色
# - font:：字体（颜色、大小）
# - width、height：控件宽度、高度
# - bd或borderwidth:外围3D边界的宽度
# 具体信息可查看源码文件__init__.py中的Label类（“Python安装目录\Lib\tkinter\__init__.py”）；
#
# ### 按钮（Button）
# 用来执行相应的功能；
# 绑定事件的方式：在按钮组件被声明时用command属性绑定，或者使用bind()方法；
# 具体信息可查看源码文件__init__.py中的Button类（“Python安装目录\Lib\tkinter\__init__.py”）；
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
