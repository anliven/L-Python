# -*- coding: utf-8 -*-
import tkinter

root = tkinter.Tk()
root.wm_title("Tkinter04 Demo")

label1 = tkinter.Label(root, text=u"账号:").grid(row=0, sticky="w")
label2 = tkinter.Label(root, text=u"密码:").grid(row=1, sticky="w")
label3 = tkinter.Label(root, text=u"")

var = tkinter.Variable()
var.set("tester")

entry1 = tkinter.Entry(root, textvariable=var)  # textvariable属性绑定变量
entry2 = tkinter.Entry(root)
entry2["show"] = "*"  # 设置show属性，实现“不可见输入”

entry1.grid(row=0, column=1, sticky="e")
entry2.grid(row=1, column=1, sticky="e")
label3.grid(row=3, column=1, sticky="w")


def reg():
    str1, str2 = entry1.get(), entry2.get()  # get()方法获取输入框的内容
    if str1 == "root" and str2 == "password":
        label3["text"] = u"登录成功"
    else:
        label3["text"] = u"用户名或密码错误"
        entry1.delete(0, len(str1))
        entry2.delete(0, len(str2))


btn = tkinter.Button(root, text=u"登录", command=reg)
btn.grid(row=2, column=1, sticky="e")

root.minsize(180, 80)
root.mainloop()

# ### grid布局
# grid()函数：
# - 参数row ：指定位于的行，从0开始；
# - 参数column ：指定位于的列，从0开始；
# - 参数sticky ：组件开始的方向，“n，s，w，e”表示上下左右；
# - 参数ipadx和ipady ：内边距的x方向与y方向，默认边距是0；
# - 参数padx和pady ：外边距的x方向与y方向，默认边距是0；
# - 参数rowspan和columnspan ：表示跨越的行数和列数；
#
# ### 注意
# pack布局和grid布局不能同时使用；
# 对于较复杂的布局，建议使用grid布局；
#
# ### 输入框（Entry）
# 获取输入的文本信息；
# 具体信息可查看源码文件__init__.py中的Entry类（“Python安装目录\Lib\tkinter\__init__.py”）；
# get()方法获取输入框的内容，使用时不需要任何参数；
