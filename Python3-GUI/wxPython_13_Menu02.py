#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "RadioMenu Demo")
        wx.Panel(self)
        menu_bar = wx.MenuBar()

        self.menu = wx.Menu()
        self.str1 = self.menu.AppendRadioItem(-1, "aaa")
        self.str2 = self.menu.AppendRadioItem(-1, "bbb")
        self.str3 = self.menu.AppendRadioItem(id=-1, item="ccc", )
        self.Bind(wx.EVT_MENU, self.onStr1, self.str1)
        self.Bind(wx.EVT_MENU, self.onStr2, self.str2)
        self.Bind(wx.EVT_MENU, self.onStr3, self.str3)
        menu_bar.Append(self.menu, "RadioItemTesting")

        self.menu2 = wx.Menu()
        self.num1 = self.menu2.AppendCheckItem(-1, "111")
        self.num2 = self.menu2.AppendCheckItem(-1, "222")
        self.num3 = self.menu2.AppendCheckItem(id=-1, item="333")
        self.Bind(wx.EVT_MENU, self.onNum1, self.num1)
        self.Bind(wx.EVT_MENU, self.onNum2, self.num2)
        self.Bind(wx.EVT_MENU, self.onNum3, self.num3)
        menu_bar.Append(self.menu2, "CheckItemTesting")

        self.menu3 = wx.Menu()
        items_count = self.menu3.Append(-1, "GetMenuItemCount", kind=wx.ITEM_CHECK)
        self.menu3.Append(-1, "testItem", kind=wx.ITEM_CHECK)
        self.Bind(wx.EVT_MENU, self.MenuItemCount2, items_count)
        menu_bar.Append(self.menu3, "AppendTesting")

        self.SetMenuBar(menu_bar)

    def onStr1(self, event):
        print("# AAA is called.")

    def onStr2(self, event):
        print("# BBB is called.")

    def onStr3(self, event):
        print("# CCC is called.")

    def onNum1(self, event):
        print("# 111 is called.")

    def onNum2(self, event):
        print("# 222 is called.")

    def onNum3(self, event):
        print("# 333 is called.")

    def MenuItemCount2(self, event):
        print("# The MenuItemCount is  : ", self.menu3.GetMenuItemCount())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 复选开关菜单项
# 菜单项模仿复选框，一个复选开关菜单项在每次被点击的时候，会在“开”与“关”状态之间转换；
# wx.Menu类的AppendCheckItem(id, text)方法：添加一个复选开关菜单项；
# wx.Menu类的InsertCheckItem(pos, id, text)方法：插入一个复选开关菜单项；
#
# ### 单选开关菜单项
# 菜单项模仿单选按钮，一个单选组中一次只允许出现一个菜单项处于“开”的状态；
# 如果在一个单选组中的另一个菜单项被选择时，先前处于“开”的菜单项会自动变成“关”的状态；
# 当单选组被创建的时候，该组中的第一个成员处于选中状态；
# wx.Menu类的AppendRadioItem(id, text)方法：添加一个单选开关菜单项；
# wx.Menu类的InsertRadioItem(pos, id, text)方法：插入一个单选开关菜单项；
#
# ### 使用Append()方法创建开关菜单项
# 设置kind参数：
# - wx.ITEM_CHECK    复选开关菜单项
# - wx.ITEM_SEPARATOR    分隔符，此时必须给id参数传递wx.ID_SEPARATOR
# - wx.ITEM_NORMAL    正常菜单
# - wx.ITEM_RADIO    单选开关菜单项
#
# ### 查看开关状态
# - 查看菜单项的开关状态：IsCheckable()
# - 设置菜单项的开关状态：Check()
# - 查看菜单项的选中状态：IsChecked()
