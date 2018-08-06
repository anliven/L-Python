# coding=utf-8
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

ttk.Label(win, text="This is a test!").grid(column=0, row=0)


def wx_app():  # wxPython function
    import wx
    app = wx.App()
    frame = wx.Frame(None, -1, "wxPython GUI", size=(200, 150))
    frame.SetBackgroundColour('white')
    frame.CreateStatusBar()
    menu = wx.Menu()
    menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
    menu_bar = wx.MenuBar()
    menu_bar.Append(menu, "File")
    frame.SetMenuBar(menu_bar)
    frame.Show()
    app.MainLoop()


action = ttk.Button(win, text=" Call wxPython GUI ", command=wx_app)
action.grid(column=0, row=1)

win.mainloop()
