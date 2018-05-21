#! python3
# -*- coding: utf-8 -*-
import tkinter
import tkinter.messagebox

root = tkinter.Tk()
root.minsize(300, 100)
root.wm_title("Tkinter07 Demo")

time_btn1 = 0


def onCbtn1():
    global show_label, time_btn1
    if time_btn1 % 2 == 0:
        show_label["text"] = "111 is selected."
    else:
        show_label["text"] = "111 is canceled."
    time_btn1 += 1


def onCbtn2():
    tkinter.messagebox.showinfo(title='Message', message='This is a Checkbutton.')


def onRbtn():
    global radio_btn
    tkinter.messagebox.showinfo(title='Message', message='This is Radiobutton.')


check_btn1 = tkinter.Checkbutton(root, text="111", command=onCbtn1)
check_btn2 = tkinter.Checkbutton(root, text="222", command=onCbtn2)
check_btn1.pack()
check_btn2.pack()

radio_btn = tkinter.Radiobutton(root, text="aaa", command=onRbtn, value="0")
radio_btn.pack()

text = tkinter.Text(root, width=30, height=10)
text.pack()
quote = "row1- This is a Text.\nrow2- This is a Text.\nrow3- This is a Text."
text.insert("end", quote)

show_label = tkinter.Label(root, text=" ")
show_label.pack()

root.mainloop()

# ### 复选按钮（Checkbutton）
# 用来选择信息；
#
# ### 单选按钮（Radiobutton）
# 用来选择信息；
#
# ### 文本域（Text）
# 相当于一个大型的文本框，但拥有更多的属性；
