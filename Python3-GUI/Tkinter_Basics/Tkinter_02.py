#! python3
# -*- coding: utf-8 -*-
import tkinter

root = tkinter.Tk()
root.wm_title("Tkinter02 Demo")

button1 = tkinter.Button(root, text="AAA").pack(side="left", expand="0", fill="y")
button2 = tkinter.Button(root, text="BBB").pack(side="top", expand="0", fill="both")
button3 = tkinter.Button(root, text="CCC").pack(side="right", expand="0", anchor="ne")
button4 = tkinter.Button(root, text="DDD").pack(side="left", expand="1", fill="y")
button5 = tkinter.Button(root, text="EEE").pack(side="top", expand="no", fill="both")
button6 = tkinter.Button(root, text="FFF").pack(side="bottom", expand="yes", fill="x")
button7 = tkinter.Button(root, text="GGG").pack(anchor="center")

root.mainloop()

# ### 布局(layout)
# - pack布局：设置少，默认从上往下按序排列；
# - grid布局：网格样式，组件的相对位置固定；
# - place布局：使用固定的位置坐标，难以改动，不推荐；
#
# ### pack布局
# pack()函数
# - 参数side : 'left', 'right', 'top', 'bottom'
# - 参数fill : 'x', 'y', 'both', 'none'
# - 参数expand : Boolean, 0 or 1
# - 参数anchor : 'n', 'e', 's', 'w', 'center'
# - 参数ipadx和ipady ：内边距的x方向与y方向
# - 参数padx和pady ：外边距的x方向与y方向
