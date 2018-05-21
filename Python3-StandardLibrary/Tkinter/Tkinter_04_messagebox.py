#! python3
# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox


class Application(tk.Frame):  # 从Frame派生一个Application类，这是所有Widget的父容器
    def __init__(self, master=None):
        super().__init__(master)
        # Frame.__init__(self, master)
        self.pack()  # pack()方法把Widget加入到父容器中，并实现布局
        self.hello_label = tk.Label(self, text='This is a label.')
        self.hello_label.pack()
        self.name_input = tk.Entry(self)
        self.name_input.pack()
        self.create_widgets()

    def create_widgets(self):
        hi_there = tk.Button(self)
        hi_there["text"] = "This is a button.\nClick"
        hi_there["command"] = self.say_hi
        hi_there.pack()
        quit_button = tk.Button(self, text="Quit", fg="red", command=root.destroy)
        # quit_button = tk.Button(self, text="Quit", fg="red", command=self.quit)  # 触发self.quit()，程序退出
        quit_button.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")
        name = self.name_input.get() or 'world'  # 获得用户输入的文本
        tk.messagebox.showinfo(title='Message', message='Hello, %s' % name)  # 弹出消息框


if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(300, 100)
    root.wm_title("Tkinter04 Demo")
    app = Application(master=root)  # 实例化Application
    app.mainloop()

# ### 消息框（messagebox）
# 具体信息可查看源码文件（“Python安装目录\Lib\tkinter\messagebox.py”）；
