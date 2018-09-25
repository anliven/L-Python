# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Text and Button Demo", wx.DefaultPosition, (300, 300))
        # 面板
        panel = wx.Panel(self, -1)  # 创建wx.Panel类的实例对象
        # 静态文本
        label = wx.StaticText(panel,  # 指定父对象
                              id=-1,
                              label="Hi, StaticText!",
                              pos=(60, 10))
        label.SetBackgroundColour("black")  # 设置背景色
        label.SetForegroundColour("white")  # 设置前景色
        # 静态文本
        text_st = wx.StaticText(panel,
                                id=-1,
                                label="Hello, wxPython!"
                                      "\n This is a test!",  # 文本换行使用“\n”转义
                                pos=(60, 40),  # 坐标位置
                                size=(120, -1),  # 文本标签的长度和宽度，这里-1表示取默认值
                                style=wx.ALIGN_CENTER)  # 居中对齐
        text_st.SetBackgroundColour("white")
        text_st.SetForegroundColour("blue")
        # 文本输入框
        text_ct = wx.TextCtrl(panel,
                              id=-1,
                              value="Input your name",
                              pos=(60, 90),
                              size=(120, -1),
                              style=wx.TE_PASSWORD)
        text_ct.SetInsertionPoint(0)  # 设置插入光标的位置
        # 按钮
        self.button = wx.Button(panel,
                                id=-1,
                                label="TestButton",
                                pos=(60, 140),
                                size=(120, -1))
        # self.button.SetLabel("Change")  # 设置按钮显示的文本信息
        # 位图按钮
        bmp = wx.Image("wxPython_04.bmp", wx.BITMAP_TYPE_BMP).ConvertToBitmap()  # 引入图片并装换为位图格式
        self.button2 = wx.BitmapButton(panel,
                                       id=-1,
                                       bitmap=bmp,  # 指定使用的位图
                                       pos=(60, 190),
                                       size=(120, -1))


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()  # 开始事件循环

# ### 控件（组件）
# 控件：窗口上的一个小型窗口，具有自己的界面并且可以执行一定的功能；
# 常用的控件包括：静态文本、面板、输入框、按钮、位图按钮等；
#
# ### 静态文本（wx.StaticText类）
# https://docs.wxpython.org/wx.StaticText.html
# 用于显示一些文本信息；
#
# ### 面板（wx.Panel类）
# https://docs.wxpython.org/wx.Panel.html
# 作为一个容器（放置所有控件），用于将窗口内容与工具栏和状态栏等分开；
#
# ### 文本输入框（wx.TextCtrl类）
# https://docs.wxpython.org/wx.TextCtrl.html
# 用于输入、显示和编辑文本信息，让用户和程序进行信息交流；
# style可以是只读（wx.TE_READONLY），多行（wx.TE_MULTILINE）或密码字段（wx.TE_PASSWORD）；
# 一些常用的方法：
# - AppendText(text)：在尾部添加文本
# - Clear()：清空文本框的信息
# - SetInsertionPoint(pos)：设置光标插入的位置，是一个从0开始的整型索引值
# - GetRange(from, to)：返回指定位置索引中间的字符串信息
# - GetValue()/SetValue()：返回/改变文本框中的字符串信息
# - Remove(from, to)：删除指定位置索引范围的文本信息
#
# ### 按钮（wx.Button类）
# https://docs.wxpython.org/wx.Button.html
# 触发设置的事件，获得响应；
# 一些常用的方法：
# - SetLabel(): 设置按钮显示的文本信息
# - GetLabel(): 获取按钮的文本信息
# - SetDefault(): 设置为对话框或窗口的默认按钮
#
# ### 位图按钮（wx.BitmapButton类）
# https://docs.wxpython.org/wx.BitmapButton.html
# 位图按钮可以指定一张图片来显示自身；
