#! python3
# -*- coding: utf-8 -*-
import wx
import time


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"这是Text Example", size=(500, 430))
        panel = wx.Panel(self)

        labelAll = wx.StaticText(panel, -1, "All Contents")
        self.textAll = wx.TextCtrl(panel, -1,
                                   size=(465, 200),
                                   style=wx.TE_MULTILINE | wx.TE_READONLY)
        self.textAll.SetInsertionPoint(0)
        labelIn = wx.StaticText(panel, -1, "I Say")
        self.textIn = wx.TextCtrl(panel, -1,
                                  size=(465, 100),
                                  style=wx.TE_MULTILINE)
        self.textIn.SetInsertionPoint(0)
        self.btnSent = wx.Button(panel, -1, "Sent", size=(75, 25))
        self.btnClear = wx.Button(panel, -1, "Clear", size=(75, 25))
        self.Bind(wx.EVT_BUTTON, self.OnButtonSent, self.btnSent)
        self.Bind(wx.EVT_BUTTON, self.OnButtonClear, self.btnClear)

        btnSizer = wx.BoxSizer()  # 创建sizer对象
        btnSizer.Add(self.btnSent, proportion=0)  # 添加部件到sizer
        btnSizer.Add(self.btnClear, proportion=0)

        mainSizer = wx.BoxSizer(wx.VERTICAL)
        mainSizer.Add(labelAll, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll, proportion=1, flag=wx.EXPAND)
        mainSizer.Add(labelIn, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textIn, proportion=0, flag=wx.EXPAND)
        mainSizer.Add(btnSizer, proportion=0, flag=wx.ALIGN_CENTER)

        panel.SetSizer(mainSizer)  # 将sizer关联到容器

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
    frame.SetMaxSize((1000, 860))  # 最大缩放尺寸
    frame.SetMinSize((250, 215))  # 最小缩放尺寸
    frame.Show()
    root.MainLoop()

# ### 布局管理器
# 布局管理器在wxPython中被称为Sizer，Wx.Sizer是所有sizer的基类；
# 使用局管理器的优点：
# - 窗口中的部件可以自动调整大小；
# - 外观均匀适配不同分辨率的显示设备；
# - 可以动态地添加或去除部件，而不需要重新设计；
#
# ### wx.BoxSizer
# 常见的sizer有wx.BoxSizer、wx.StaticBoxSizer、wx.GridSizer、wx.FlexGridSizer和wx.GridBagSizer等；
# wx.BoxSizer：控件位置按行或列的方式，布局由定位参数(wxVERTICAL或wxHORIZONTAL)确定；
