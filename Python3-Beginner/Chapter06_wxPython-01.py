#! python3
# -*- coding: utf-8 -*-
import wx

app = wx.App()  # 创建应用程序对象
frame = wx.Frame(parent=None)  # 生成框架窗口
frame.Show()  # 显示框架窗口
app.MainLoop()  # 进入消息循环

# ### 对象化开发 - 适用于简单窗口创建
# - 生成应用程序对象和框架对象；
# - 直接使用wx.App、wx.Frame等相关类的方法；
