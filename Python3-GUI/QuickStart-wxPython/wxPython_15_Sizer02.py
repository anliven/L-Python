# -*- coding: utf-8 -*-
import wx


class TextFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"这是StaticBoxSizer Demo", size=(300, 300))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(orient=wx.VERTICAL)  # 创建BoxSizer对象

        box1 = wx.StaticBox(parent=panel, id=-1, label="String")  # 创建静态框
        sizer1 = wx.StaticBoxSizer(box=box1, orient=wx.VERTICAL)  # 创建StaticBoxSizer对象
        for item in ["aaa", "bbb", "ccc"]:
            btn = wx.Button(box1, -1, item)
            sizer1.Add(btn)

        box2 = wx.StaticBox(panel, -1, "Number")  # 使用StaticBoxSizer之前通常使用StaticBox
        sizer2 = wx.StaticBoxSizer(box=box2, orient=wx.VERTICAL)
        for item in ["111", "222", "333"]:
            btn = wx.Button(box2, -1, item)
            sizer2.Add(btn)

        sizer.Add(sizer1)  # sizer的嵌套，添加的是布局管理器
        sizer.Add(sizer2)  # 实现的效果：sizer1和sizer2的内部是StaticBox布局，但它们之间是Box布局
        panel.SetSizer(sizer)  # 将sizer关联到容器


if __name__ == '__main__':
    root = wx.App()
    frame = TextFrame()
    frame.SetMaxSize((600, 600))  # 最大缩放尺寸
    frame.SetMinSize((300, 300))  # 最小缩放尺寸
    frame.Show()
    root.MainLoop()

# ### 静态框（StaticBox类）
# https://docs.wxpython.org/wx.StaticBox.html
#
# ### wx.StaticBoxSizer
# https://docs.wxpython.org/wx.StaticBoxSizer.html
# 可以使用静态框在sizer周围提供一个边框和文本标签；
