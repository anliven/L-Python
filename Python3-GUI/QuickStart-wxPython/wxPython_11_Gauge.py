# -*- coding: utf-8 -*-
import wx
import time


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Gauge Demo", wx.DefaultPosition, (400, 300))
        panel = wx.Panel(self)

        self.label = wx.StaticText(panel, -1, "Download: ", (20, 20), (70, 25))
        self.count = 20
        self.gauge = wx.Gauge(panel, -1, 100, (100, 20), (200, 25), wx.HORIZONTAL)
        self.gauge.SetValue(self.count)
        self.gauge.Bind(wx.EVT_IDLE, self.onIdle)

        self.label2 = wx.StaticText(panel, -1, "Speed: ", (20, 60), (70, 25))
        self.count2 = 10
        self.gauge2 = wx.Gauge(parent=panel,
                               id=-1,
                               range=100,
                               pos=(80, 60),
                               size=(25, 150),
                               style=wx.GA_VERTICAL
                               )
        self.gauge2.SetValue(self.count2)
        self.gauge2.Bind(wx.EVT_IDLE, self.onIdle2)

    def onIdle(self, event):
        if self.count < 100:
            self.count += 10
            time.sleep(0.5)
            self.gauge.SetValue(self.count)

    def onIdle2(self, event):
        if self.count2 < 100:
            self.count2 += 10
            time.sleep(0.2)
            self.gauge2.SetValue(self.count2)


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 进度条（wx.Gauge类）
# https://docs.wxpython.org/wx.Gauge.html
