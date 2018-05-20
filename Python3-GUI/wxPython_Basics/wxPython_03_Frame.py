#! python3
# -*- coding: utf-8 -*-
import wx


class MyApp(wx.App):  # 自定义App类，继承自wx.App
    def __init__(self):  # 自定义__init__方法
        wx.App.__init__(self)

    def OnInit(self):  # 重写方法，程序开始时自动被调用，不需要任何参数
        self.frame = wx.Frame(parent=None,
                              id=-1,
                              title="Frame Demo",
                              pos=wx.DefaultPosition,
                              size=wx.DefaultSize,
                              style=wx.DEFAULT_FRAME_STYLE,
                              name="frame")  # 生成框架窗口
        self.frame.Show()  # 显示框架窗口
        self.SetTopWindow(self.frame)  # 为应用程序指定一个顶级窗口
        print("Hi!")
        return True  # 返回一个布尔值：如果返回True，程序正常向下执行，如果返回False，程序退出

    def OnExit(self):  # 与OnInit方法对应，当最后一个窗口被关闭且在应用程序的清理过程(释放资源)之前被调用
        print("Bye!")
        return True


if __name__ == "__main__":
    app = MyApp()  # 创建类实例，这里OnInit()自动被调用
    app.MainLoop()  # 开始事件循环

# ### wx.App类
# https://docs.wxpython.org/wx.App.html
#
# ### wx.Frame类
# https://docs.wxpython.org/wx.Frame.html
#
# ### wx.App的OnInit与OnExit()方法
# - OnInit()方法 : 程序开始时自动被调用，不需要任何参数
# - OnExit()方法 : 如果调用了全局的Exit()方法来关闭应用程序，那么该方法会被自动触发
#
# ### wx.Frame的__init__方法常用参数
# - parent=None ： 指定父对象，如果取值为None则表示为顶级窗口
# - id=-1 ： 窗口内子部件的唯一标识，每个窗口内的子部件的ID必须是唯一的
# - title="Test" ： 窗口的标题
# - pos=wx.DefaultPosition ： 坐标位置，如果取值为(-1, -1)将采用系统默认的位置
# - size=wx.DefaultSize ： 窗口大小（长度与宽度），如果取值为(-1, -1)将采用系统默认的大小
# - style=wx.DEFAULT_FRAME_STYLE : 显示格式风格
# - name="frame" ： 窗口的标识，可用于查找此窗口
