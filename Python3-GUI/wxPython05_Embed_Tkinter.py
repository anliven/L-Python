# coding=utf-8
import wx


def tk_app():  # Tkinter function
    import tkinter as tk
    from tkinter import ttk
    win = tk.Tk()
    win.title("Python GUI")
    ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
    name = tk.StringVar()
    name_entered = ttk.Entry(win, width=12, textvariable=name)
    name_entered.grid(column=0, row=1)
    name_entered.focus()

    def btn_callback():
        action.configure(text='Hello ' + name.get())

    action = ttk.Button(win, text="Print", command=btn_callback)
    action.grid(column=2, row=1)
    win.mainloop()


app = wx.App()
frame = wx.Frame(None, -1, "wxPython GUI", size=(200, 100))
frame.SetBackgroundColour('white')
frame.CreateStatusBar()


def write_to_shared_queue(event):
    tk_app()


button = wx.Button(frame, label="Call tkinter GUI", pos=(0, 30))
frame.Bind(wx.EVT_BUTTON, write_to_shared_queue, button)
frame.Show()

app.MainLoop()
