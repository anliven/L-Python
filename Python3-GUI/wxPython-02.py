#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):  # 继承wx.Frame类
    pass


class MyApp(wx.App):  # 继承wx.App类
    def OnInit(self):  # 重写方法
        frame = MyFrame(parent=None)  # 生成框架窗口
        frame.Show()  # 显示框架窗口
        return True


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()  # 进入消息循环

# ### 子类化开发 - 复杂程序开发
# 根据具体需求，继承wx.App、wx.Frame等类，重写方法；
