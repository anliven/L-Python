#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "CheckListBox Demo", wx.DefaultPosition, (300, 200))
        panel = wx.Panel(self)
        # 复选列表框
        mylist1 = ["aaa", "bbb", "ccc", "ddd", "eee"]
        mylist2 = ["111", "222", "333", "444", "555"]
        self.clb1 = wx.CheckListBox(panel, -1, (20, 20), (100, 60), mylist1)
        self.clb2 = wx.CheckListBox(parent=panel,
                                    id=-1,
                                    pos=(150, 20),
                                    size=(100, 60),
                                    choices=mylist2)
        self.clb1.SetSelection(0)
        self.clb2.SetSelection(2)
        self.clb1.Bind(wx.EVT_CHECKLISTBOX, self.onCheckListBox1)
        self.clb2.Bind(wx.EVT_CHECKLISTBOX, self.onCheckListBox2)

    def onCheckListBox1(self, event):
        print("$ CheckListBox One", self.clb1.GetCheckedItems())

    def onCheckListBox2(self, event):
        print("$ CheckListBox Two", self.clb2.GetCheckedItems())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 复选列表框（CheckListBox类）
# https://docs.wxpython.org/wx.CheckListBox.html
# 选项放在一个矩形的窗口中，用户可以选择其中的一个或者多个；
# 常用函数与ListBox类相似；
