#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Menu01 Demo")
        wx.Panel(self)

        menu_bar = wx.MenuBar()  # 创建菜单栏，不需要任何参数

        self.menu1 = wx.Menu()  # 创建菜单
        self.str1 = self.menu1.Append(-1, "aaa")  # 在菜单中创建菜单项
        self.str2 = self.menu1.Append(-1, "bbb")  # Append方法的返回值是一个MenuItem实例
        self.str3 = self.menu1.Append(id=-1,  # id 用于标识独一无二的一个菜单项
                                      item="Count",
                                      helpString="Get menu item count")
        self.Bind(wx.EVT_MENU, self.MenuItemCount1, self.str3)  # 菜单项绑定事件
        menu_bar.Append(self.menu1, "String")  # 菜单附加到菜单栏

        self.menu2 = wx.Menu()
        items_count = self.menu2.Append(-1, "GetMenuItemCount")
        self.Bind(wx.EVT_MENU, self.MenuItemCount2, items_count)
        menu_bar.Append(self.menu2, "Test")

        self.SetMenuBar(menu_bar)  # 设置窗口的菜单栏

    def MenuItemCount1(self, event):
        print("# The MenuItemCount is  : ", self.menu1.GetMenuItemCount())

    def MenuItemCount2(self, event):
        print("# The MenuItemCount is  : ", self.menu2.GetMenuItemCount())


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 菜单
# 分类：菜单栏菜单，也就是常规菜单；弹出式菜单（右键菜单/上下文菜单），点击鼠标右键出现的菜单；
# 菜单包含菜单项，菜单项可以包含子菜单；
# 主要涉及三个类：
# - wx.MenuBar ：用于处理菜单栏
# - wx.Menu ：用于管理一个下拉菜单或弹出菜单
# - wx.MenuItem ：用于管理具体的菜单项
#
# ### 菜单栏（wx.MenuBar类）
# https://docs.wxpython.org/wx.MenuBar.html
# 主要方法：
# - Append(menu, title) ：向菜单栏的尾部添加一个菜单
# - Insert(pos, Menu, title) ：向菜单栏的指定位置（从0开始的索引)添加一个菜单
# - Remove(pos) ：删除索引为pos的菜单
# - GetMenuCount() ：返回当前菜单栏的菜单个数
# - Replace(pos, Menu, title) ：使用相应的菜单去替换指定位置的菜单
# - GetMenu(pos) ：返回指定位置的菜单对象
# - GetLabelTop(pos) ：返回指定位置的菜单标签
# - SetLabelTop(pos, label) ：设置指定位置的菜单标签
# - FindMenu(title) ：返回菜单栏中指定名称菜单的索引
# - EnableTop(pos, enable) ：设置指定位置的菜单是否可用
#
# ### 菜单（wx.Menu类）
# https://docs.wxpython.org/wx.Menu.html
# 主要方法：
# - Append() ：向菜单添加一个菜单项
# - Insert() ：向菜单的指定位置添加一个菜单项
# - AppendSeparator(pos) ：向菜单的指定位置添加一个分割线
# - InsertSeparator(pos) ：向菜单的指定位置插入一个分割线
# - Remove(id) ：删除指定ID的菜单项
# - GetMenuItemCount() ：返回菜单中的菜单项个数
# - GetMenuItems() ： 返回菜单中项目的一个列表
#
# ### 菜单项（wx.MenuItem类）
# https://docs.wxpython.org/wx.MenuItem.html
#
# ### Enable()方法与IsEnabled()方法
# Enable()方法：设置菜单栏、菜单、菜单项是否可用；
# - 菜单栏：Enable(self, id, enable)
# - 菜单：Enable(self, id, enable)
# - 菜单项：Enable(self, enable=True)
# IsEnabled()方法：查看是否可用；
# - 菜单栏：IsEnable(id)
# - 菜单：IsEnable(id)
# - 菜单项：IsEnable()
# 另外，wx.MenuBar类的EnableTop(pos, enable)方法可以设置整个顶级菜单有效或无效；
