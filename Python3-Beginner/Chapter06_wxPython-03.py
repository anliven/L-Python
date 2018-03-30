#! python3
# -*- coding: utf-8 -*-
import wx
from turtle import Turtle


class MyApp(wx.App):  # 继承wx.App类
    def OnInit(self):  # 重写方法
        frame = wx.Frame(parent=None,
                         title="This is a test!",
                         size=(385, 200),
                         pos=(800, 300)
                         )  # 生成框架窗口
        panel = wx.Panel(frame, -1)  # 生成面板
        self.buttonWJX = wx.Button(panel,
                                   -1,
                                   "五角星",
                                   size=(75, 25),
                                   pos=(5, 5))
        self.Bind(wx.EVT_BUTTON, self.OnButtonWJX, self.buttonWJX)
        frame.Show()  # 显示框架窗口
        return True

    def OnButtonWJX(self, event):
        t = Turtle()
        for i in range(5):
            t.forward(150)
            t.right(144)


if __name__ == "__main__":
    app = MyApp()
    app.MainLoop()  # 进入消息循环

# ### 框架（类）
# 面板（容器）--->
# - 组件1 + 事件响应---> 组件2 + 事件响应 ---> ......
# - 菜单 + 菜单项1 + 菜单项2 + ......
# - 对话框1 + 对话框2 + ......
# - ......
#
# ### 组件（类）
# - 标签
# - 按钮
# - 事件处理
# - 文本框
# - Sizer
# - ......
#
# ### 布局
# - 大小：size(x,y)
# - 位置：pos(x,y)
