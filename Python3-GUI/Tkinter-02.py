#! python3
# -*- coding: utf-8 -*-
from tkinter import *
import tkinter.messagebox as messagebox


class Application(Frame):  # 从Frame派生一个Application类，这是所有Widget的父容器
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()  # pack()方法把Widget加入到父容器中，并实现布局
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='This is a sample.')  # 创建一个Label
        self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hi', command=self.hello)  # 创建一个Button，点击按钮，触发hello()
        self.alertButton.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)  # 点击按钮，触发self.quit()，程序退出
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'  # 获得用户输入的文本
        messagebox.showinfo('Message', 'Hello, %s' % name)  # 弹出消息对话框


app = Application()  # 实例化Application
app.master.title('Hello World')  # 设置窗口标题
app.mainloop()  # 主消息循环