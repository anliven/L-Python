# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Slider Demo", wx.DefaultPosition, (400, 300))
        panel = wx.Panel(self)

        self.label = wx.StaticText(panel, -1, "Download: ", (20, 20), (70, 25))
        self.slider = wx.Slider(panel, -1, 0, 1, 100, (100, 20), (200, 25))  # 默认水平方向（wx.SL_HORIZONTAL）
        self.slider.Bind(wx.EVT_SCROLL, self.onScroll)

        self.label2 = wx.StaticText(panel, -1, "Speed: ", (20, 60), (70, 25))
        self.slider2 = wx.Slider(parent=panel,
                                 id=-1,
                                 value=20,  # 初始值
                                 minValue=1,  # minvalue表示最小值，maxvalue表示最大值
                                 maxValue=100,
                                 pos=(80, 60),
                                 size=(25, 150),
                                 style=wx.SL_VERTICAL)  # wx.SL_VERTICAL表示竖直方向
        self.slider2.Bind(wx.EVT_SCROLL, self.onScroll2)

    def onScroll(self, event):
        print("# The current value of Download : ", self.slider.GetValue())

    def onScroll2(self, event):
        print("$ The current value of Speed : ", self.slider2.GetValue())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 滑块（wx.Slider类）
# https://docs.wxpython.org/wx.Slider.html
# 创建滑块时，通常指定parent、id、value、minvalue、maxvalue、pos、size、style等参数；
# 滑块的主要事件类型：
# - wx.EVT_SCROLL : 任何拖动事件都会触发
# - wx.EVT_SCROLL_LINEDOWN : 向下滑动一格
# - wx.EVT_SCROLL_LINEUP : 向上滑动一格
# - wx.EVT_SCROLL_BOTTOM : 移动到滑块的最末端时触发
# - wx.EVT_SCROLL_TOP : 移动到滑块的最顶端时触发
