#! python3
# -*- coding: utf-8 -*-
import wx

app = wx.App()  # 创建wx.App应用实例对象
frame = wx.Frame(None, -1, "Test")  # 创建wx.Frame窗口实例对象：生成顶层框架窗口和设置标题
frame.Show()  # 显示框架窗口
app.MainLoop()  # 进入消息循环（接受各种事件，并作出相应的反应）

# ### GUI（Graphical User Interface）
# 图形用户接口：采用图形方式显示的计算机操作环境用户接口；
#
# ### wxPython
# 开源的、免费的、跨平台的GUI库，是C++类库wxWidgets的Python版本；
#
# ### 对象化开发
# 适用于简洁的GUI程序创建，直接使用wx.App、wx.Frame等相关类的方法；
# wxPython程序最基本的部分包含：生成app应用程序对象和frame框架窗口对象；
# 为了避免数据和界面过度耦合而难以维护，建议：
# - 处理数据信息放置在wx.App应用实例对象；
# - 绘制显示的部分放置在wx.Frame窗口实例对象；
