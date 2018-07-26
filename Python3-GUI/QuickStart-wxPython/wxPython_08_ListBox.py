#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "List Demo", wx.DefaultPosition, (300, 200))
        panel = wx.Panel(self)
        # 单选列表框
        mylist1 = ["aaa", "bbb", "ccc", "ddd", "eee"]
        mylist2 = ["111", "222", "333", "444", "555"]
        self.lb1 = wx.ListBox(panel, -1, (20, 20), (100, 60), mylist1, wx.LB_SINGLE)
        self.lb2 = wx.ListBox(parent=panel,
                              id=-1,
                              pos=(150, 20),
                              size=(100, 60),
                              choices=mylist2,
                              style=wx.LB_MULTIPLE)  # LB_SINGLE表示只能从列表框中选择一个，LB_MULTIPLE可以选择多个
        self.lb1.SetSelection(0)  # 指定列表框的第一个选项被选中
        self.lb2.SetSelection(2)
        self.lb1.Bind(wx.EVT_LISTBOX_DCLICK, self.onListBox1)  # 双击触发wx.EVT_LISTBOX_DCLICK事件
        self.lb2.Bind(wx.EVT_LISTBOX, self.onListBox2)  # 单击（被选择）触发wx.EVT_LISTBOX事件

    def onListBox1(self, event):
        print("# ListBox One: ", self.lb1.GetSelection())

    def onListBox2(self, event):
        print("# ListBox Two: ", self.lb2.GetSelections())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 单选列表框（wx.ListBox类）
# https://docs.wxpython.org/wx.ListBox.html
# 选项放在一个矩形的窗口中，用户可以选择其中的一个；
# 常用函数(用于获取用户的选择信息)：
# - GetSelection() - 返回当前被选择的索引，从0开始的整数
# - GetSelections() - 返回包含所选项目位置的整数列表
# - GetStringSelection() - 返回被选中的字符串表示
# - Selected(n) - 返回索引为n的项目是否被选中（布尔值）
# - SetSelection(n) - 设置索引为n的项目被选中
# - Clear() - 清空列表框
# - Delete(n) - 删除列表框中索引为n的项目
