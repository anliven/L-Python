#! python3
# -*- coding: utf-8 -*-
from tkinter import *  # 必须添加此引用
import tkinter.messagebox
from tkinter.ttk import *  # 必须添加此引用


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.hello_label = Label(self, text='This is a label.', style="BW.TLabel")  # style属性
        self.hello_label.pack()
        self.name_input = Entry(self)
        self.name_input.pack()
        self.create_widgets()

    def create_widgets(self):
        hi_there = Button(self)
        hi_there["text"] = "This is a button.\nClick"
        hi_there["command"] = self.say_hi
        hi_there.pack()
        quit_button = Button(self, text="Quit", command=self.quit)
        quit_button.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        name = self.name_input.get() or 'world'
        tkinter.messagebox.showinfo(title='Message', message='Hello, %s' % name)


if __name__ == "__main__":
    app = Application()
    style = Style()  # 在ttk中通过style对象来实现Tkinter中的fg和bg
    style.configure("BW.TLabel", foreground="black", background="white")
    app.master.title('Hello World')  # 设置窗口标题
    app.mainloop()

# ### tkinter.ttk
# Tk themed widgets
# https://docs.python.org/3/library/tkinter.ttk.html
# ttk组件是为了解决tkinter界面简陋、控件有限、布局困难等缺点而引入的；
#
# ### 特别注意
# - ttk中很多组件与Tkinter相同，在这种情况下，ttk将覆盖Tkinter组件；
# - ttk中某些属性与tkinter存在差异；
