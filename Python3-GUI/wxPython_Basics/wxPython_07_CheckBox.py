#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Check Demo", wx.DefaultPosition, (300, 200))
        panel = wx.Panel(self)
        # 复选框
        self.check1 = wx.CheckBox(panel, -1, "football", (60, 60), (150, 20))
        self.check2 = wx.CheckBox(panel, -1, "tennis", (60, 80), (150, 20))
        self.check1.Bind(wx.EVT_CHECKBOX, self.onCheck1)
        self.check2.Bind(wx.EVT_CHECKBOX, self.onCheck2)

    def onCheck1(self, event):
        print("# Love football. - ", self.check1.GetValue())  # GetValue方法判断该复选框是否被选中

    def onCheck2(self, event):
        print("$ Love tennis. - ", self.check2.IsChecked())  # GetValue方法与IsChecked方法效果相同


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 复选框（wx.CheckBox类）
# https://docs.wxpython.org/wx.CheckBox.html
# 带有文本标签的开关按钮，可以同时选中复选框的多个选项；
