# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Menu03 Demo")
        self.panel = wx.Panel(self)
        menu_bar = wx.MenuBar()

        # 菜单
        self.menu = wx.Menu()
        self.str1 = self.menu.Append(-1, "aaa")
        self.str2 = self.menu.Append(-1, "bbb")
        self.str3 = self.menu.Append(-1, "ccc")
        # 子菜单
        self.subMenu = wx.Menu()
        self.num1 = self.subMenu.AppendCheckItem(-1, "111")
        self.num2 = self.subMenu.AppendCheckItem(-1, "222")
        self.num3 = self.subMenu.AppendCheckItem(-1, "333")
        self.Bind(wx.EVT_MENU, self.onNum1, self.num1)
        self.Bind(wx.EVT_MENU, self.onNum2, self.num2)
        self.Bind(wx.EVT_MENU, self.onNum3, self.num3)
        self.menu.AppendSubMenu(self.subMenu, "Number")  # 添加子菜单

        menu_bar.Append(self.menu, "SubMenuTesting")
        self.SetMenuBar(menu_bar)

        # 弹出式菜单
        self.popMenu = wx.Menu()
        for title in ["!!!", "@@@", "###"]:
            self.popMenu.Append(-1, title)
        self.Bind(wx.EVT_CONTEXT_MENU, self.onPop)  # 绑定鼠标右键事件
        self.popMenu.Bind(wx.EVT_CONTEXT_MENU, self.onPop)

        # 状态栏
        status_bar = self.CreateStatusBar()  # 创建状态栏，返回一个StatusBar的实例
        status_bar.SetStatusText("This is an status bar.")  # 设置显示信息

    def onNum1(self, event):
        print("# 111 is called.")

    def onNum2(self, event):
        print("# 222 is called.")

    def onNum3(self, event):
        print("# 333 is called.")

    def onPop(self, event):
        print("# PopupMenu is called.")
        pos = event.GetPosition()  # 当前鼠标相对于屏幕左上角的坐标
        scrpos = self.panel.ScreenToClient(pos)  # 转化为客户区的坐标
        self.panel.PopupMenu(self.popMenu, scrpos)  # PopupMenu()方法弹出菜单


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 子菜单
# wx.Menu类的AppendSubMenu(self, submenu, text, help="")方法用于添加一个子菜单；
#
# ### 弹出式菜单
# 点击鼠标右键的时候出现的菜单，也称为右键菜单或者上下文菜单；
# 弹出式菜单和普通的菜单一样可以响应事件；
# - wx.EVT_CONTEXT_MENU ：鼠标右键点击之后的触发事件
# - event.GetPosition()：相对于屏幕的左上角(0, 0)的坐标
# - ScreenToClient(pos) ：转化为客户区（可以自由操作的部分）的坐标
# - Panel类的PopupMenu() ：弹出菜单
#
# ### 状态栏
# 创建一个状态栏并且显示相应的文本信息；
# https://docs.wxpython.org/wx.StatusBar.html
# - CreateStatusBar() ：创建状态栏，返回一个StatusBar的实例
# - StatusBar类SetStatusText() ： 设置显示信息
