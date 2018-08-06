# coding=utf-8
import tkinter as tk
from tkinter import ttk
from threading import Thread
from multiprocessing import Queue
import wx

win = tk.Tk()
win.title("Python GUI")

text = tk.Text(win, height=10, width=40, borderwidth=2, wrap='word')
text.grid(column=0, row=1, sticky='WE', columnspan=3)

sharedQueue = Queue()  # from queue import Queue
dataInQueue = False


def put_data_into_queue(data):
    global dataInQueue
    dataInQueue = True
    sharedQueue.put(data)


def read_data_from_queue():
    global dataInQueue
    dataInQueue = False
    return sharedQueue.get()


class GUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        button = wx.Button(self, label="Print", pos=(0, 85))
        self.Bind(wx.EVT_BUTTON, self.write_to_shared_queue, button)
        self.textBox = wx.TextCtrl(self, size=(300, 80), style=wx.TE_MULTILINE)

    def write_to_shared_queue(self, event):
        self.textBox.AppendText("The Print Button has been clicked!\n")
        put_data_into_queue('Hi from wxPython via Shared Queue.\n')
        if dataInQueue:
            data = read_data_from_queue()
            self.textBox.AppendText(data)
            text.insert('0.0', data)  # insert data into tkinter GUI


def wx_app():
    app = wx.App()
    frame = wx.Frame(None, title="Python GUI using wxPython", size=(300, 150))
    GUI(frame)
    frame.Show()
    run_test = Thread(target=app.MainLoop)
    run_test.setDaemon(True)
    run_test.start()
    print(run_test)
    print('createThread():', run_test.isAlive())


action = ttk.Button(win, text="Call wxPython GUI", command=wx_app)
action.grid(column=0, row=0, sticky="w")

win.mainloop()
