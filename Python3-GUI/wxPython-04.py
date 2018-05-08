#! python3
# -*- coding: utf-8 -*-
import wx
import time


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"这是Text Example", size=(500, 430))
        wx.StaticText(self, -1, "All Contents", pos=(200, 0))
        self.textAll = wx.TextCtrl(self, -1,
                                   size=(465, 200),
                                   pos=(10, 25),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.textAll.SetInsertionPoint(0)
        wx.StaticText(self, -1, "I Say", pos=(220, 230))
        self.textIn = wx.TextCtrl(self, -1,
                                  size=(465, 100),
                                  pos=(10, 255),
                                  style=wx.TE_MULTILINE)
        self.textIn.SetInsertionPoint(0)
        self.btnSent = wx.Button(self, -1, "Sent", size=(75, 25), pos=(160, 360))
        self.btnClear = wx.Button(self, -1, "Clear", size=(75, 25), pos=(260, 360))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSent, self.btnSent)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClear, self.btnClear)

    def OnButtonSent(self, event):
        userinput = self.textIn.GetValue()
        self.textIn.Clear()
        now = time.ctime()
        inmsg = "You (%s):\n%s \n" % (now, userinput)
        self.textAll.AppendText(inmsg)

    def OnButtonClear(self, event):
        self.textIn.Clear()


if __name__ == '__main__':
    root = wx.App()
    frame = TextFrame()
    frame.Show()
    root.MainLoop()

# ### 文本框
# wx.TextCtrl类实现文本框功能，可以输入、显示和编辑文本；
# TextCtrl部件可以是只读（wx.TE_READONLY），多行（wx.TE_MULTILINE）或密码字段（wx.TE_PASSWORD）;
