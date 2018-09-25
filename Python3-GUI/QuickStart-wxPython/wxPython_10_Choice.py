# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Choice Demo", wx.DefaultPosition, (300, 200))
        panel = wx.Panel(self)

        wx.StaticText(panel, -1, "Letter: ", (10, 10), (50, 20))
        mylist1 = ["aaa", "bbb", "ccc", "ddd", "eee"]
        self.c1 = wx.Choice(panel, -1, (60, 10), (60, 60), choices=mylist1)
        self.c1.Bind(wx.EVT_CHOICE, self.onChoice1)

        wx.StaticText(panel, -1, "Number: ", (140, 10), (50, 20))
        mylist2 = ["111", "222", "333", "444", "555"]
        self.c2 = wx.Choice(parent=panel,
                            id=-1,
                            pos=(200, 10),
                            size=(60, 60),
                            choices=mylist2)
        self.c2.Bind(wx.EVT_CHOICE, self.onChoice2)

    def onChoice1(self, event):
        print("$ letter: ", self.c1.GetCurrentSelection())  # 获得该选项的索引

    def onChoice2(self, event):
        print("$ number: ", self.c2.GetStringSelection())  # 获得该选项的字符串信息


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 下拉选项（wx.Choice类）
# https://docs.wxpython.org/wx.Choice.html
# 选项放在一个下拉菜单中，用户可以选择其中的一个或者多个；
# 常用函数与ListBox类相似；
