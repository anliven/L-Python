# -*- coding: utf-8 -*-
import wx
import time


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"这是BoxSizer Demo", size=(500, 430))
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

        btnSizer = wx.BoxSizer()  # 创建BoxSizer对象
        btnSizer.Add(self.btnSent, proportion=0)  # 添加部件到sizer
        btnSizer.Add(self.btnClear, proportion=0)

        mainSizer = wx.BoxSizer(orient=wx.VERTICAL)  # 垂直排列
        mainSizer.Add(labelAll, proportion=0, flag=wx.ALIGN_CENTER)
        mainSizer.Add(self.textAll, proportion=1, flag=wx.EXPAND)  # wx.EXPAND跟随sizer的尺寸变化
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

# ### 布局
# 布局：将涉及的部件合理放置，并友好的显示；
# 最直接的办法是指定绝对位置：在创建部件时通过参数size(x,y)和pos(x,y)指定大小和位置；
# 但对于复杂的布局，随着部件书目的增多，难以有效的处理众多参数size(x,y)和pos(x,y)之间的关系；
#
# ### 布局管理器（wx.Sizer类）
# https://docs.wxpython.org/wx.Sizer.html
# 布局管理器在wxPython中被称为Sizer，是用于自动布局一组窗口部件的算法，wx.Sizer是所有sizer的基类；
# 布局管理器的优点：
# - 能够完成复杂的布局；
# - 窗口和窗口中的部件可以自动调整大小；
# - 外观均匀适配不同分辨率的显示设备；
# - 可以动态地添加或去除部件，而不需要重新设计；
#
# ### 分类
# 常见的sizer有wx.BoxSizer、wx.StaticBoxSizer、wx.GridSizer、wx.FlexGridSizer和wx.GridBagSizer等；
# 大致分为类似线性布局（Box）和网格布局（Grid）；
# - Box ：线性布局，在水平或竖直方向上放置窗口部件，可以适应大小的改变；
# - StaticBox ：带有标题和环线；
# - Grid ：网格布局，窗口部件都以同样的尺寸整齐的放入规定的网格中；
# - FlexGrid ：是对Grid的一个加强，可以适应窗口部件的不同尺寸；
# - GridBag ：可以使网格中的窗口部件更随意的设置自己的位置；
#
# ### 使用步骤
# - 1 创建一个sizer并将sizer附加到面板（也就是关联到一个容器）；
# - 2 将部件添加到sizer（通过SetSizer(sizer)方法设置布局，使用sizer的Add()方法添加部件到sizer）；
# - 3 sizer管理所包含的部件(Fit()、Insert()、 Detach()等方法)；
#
# ### wx.BoxSizer
# https://docs.wxpython.org/wx.BoxSizer.html
# 窗口部件位置按行或列的方式布置在一条线上，布局由定位参数(wxVERTICAL或wxHORIZONTAL)确定；
