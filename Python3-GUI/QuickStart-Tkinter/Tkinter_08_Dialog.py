# -*- coding: utf-8 -*-
import tkinter
import tkinter.dialog

root = tkinter.Tk()
root.wm_title("Tkinter08 Demo")
root.minsize(300, 100)


def onDialog():
    dlg = tkinter.dialog.Dialog(master=None,
                                title="",
                                text="擅长的编程语言？",
                                bitmap=tkinter.dialog.DIALOG_ICON,
                                default=0,
                                strings=("Python", "Shell", "Java"))
    print(dlg.num)  # num属性返回用户的点击


btn1 = tkinter.Button(text="开始参与调查", command=onDialog)
btn1.pack()
btn2 = tkinter.Button(text="退出并关闭", command=btn1.quit)
btn2.pack()

root.mainloop()

# ### 对话框（Dialog）
# 具体信息可查看源码文件（“Python安装目录\Lib\tkinter\dialog.py”）；
# 其他标准对话框：simpledialog（简单对话框）、commondialog（一般对话框）、filedialog（文件对话框）等；
