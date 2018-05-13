#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Radio Demo", wx.DefaultPosition, (300, 300))
        panel = wx.Panel(self)
        # 单选框
        wx.RadioButton(panel, -1, "AAA", (60, 10), style=wx.RB_GROUP)  # RB_GROUP表示一个组的开始
        wx.RadioButton(panel, -1, "BBB", (60, 30))  # 归属于上一个RB_GROUP
        self.radio3 = wx.RadioButton(panel, -1, "aaa", (60, 60), style=wx.RB_GROUP)  # 新的RB_GROUP表示一个新组的开始
        self.radio4 = wx.RadioButton(panel, -1, "bbb", (60, 80))
        self.radio3.Bind(wx.EVT_RADIOBUTTON, self.onRadio1)
        self.radio4.Bind(wx.EVT_RADIOBUTTON, self.onRadio2)
        # 单选框组合
        list1 = ["radio5", "radio6"]
        list2 = ['radio7', 'radio8']
        self.rb1 = wx.RadioBox(panel, -1, "Group One", (60, 110), wx.DefaultSize, list1, 2, wx.RA_SPECIFY_COLS)
        self.rb2 = wx.RadioBox(parent=panel,  # 父对象
                               id=-1,  # ID
                               label="Group Two",  # 标签名，可以省略
                               pos=(60, 170),  # 位置
                               size=wx.DefaultSize,  # 大小
                               choices=list2,  # 使用的列表
                               majorDimension=2,  # 显示的行数或列数
                               style=wx.RA_SPECIFY_ROWS)  # 样式
        self.rb1.Bind(wx.EVT_RADIOBOX, self.onRadioBox1)
        self.rb2.Bind(wx.EVT_RADIOBOX, self.onRadioBox2)

    def onRadio1(self, event):
        print("# aaa - ", self.radio3.GetValue())

    def onRadio2(self, event):
        print("$ bbb - ", self.radio4.GetValue())

    def onRadioBox1(self, event):
        print("# list1 - ", self.rb1.GetSelection())

    def onRadioBox2(self, event):
        print("$ list2 - ", self.rb2.GetSelection())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 控件
# 使用已有控件可以简洁地创建一些界面，简化GUI编程；
# 标准控件包括单选框、复选框、列表框、组合框等；
#
# ### 单选框（wx.RadioButton类）
# https://docs.wxpython.org/wx.RadioButton.html
# 多个选项中选择其中的一个时，其他的选项会自动被设置为未选中状态；
#
# ### 单选框分组（wx.RadioBox类）
# https://docs.wxpython.org/wx.RadioBox.html
# 相关的单选框放置在同一组，但只能选择其中的一个选项，其他的单选框会自动被设置为未选中状态；
# 常用函数：
# - GetCount() - 返回单选框分组中选项的数量
# - FindString(string) - 根据给定的标签返回相关按钮的整数索引值，如果标签不存在，则返回-1
# - EnabelItem(n,flag) - 设置索引为n的按钮是否有效，flag是一个布尔值
# - SetItemLabel(n,string) - 设置索引为n的按钮的字符串标签
# - GetItemLabel(n) - 获取索引为n的按钮的字符串标签
# - GetSelection() - 获取被选择的整数索引
# - GetStringSelection() - 获取被选择的字符串信息
# - SetSelection(n) - 使索引为n的单选框被选中
