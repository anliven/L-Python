# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, u"这是GridBagSizer Demo")
        panel = wx.Panel(self)
        sizer = wx.GridBagSizer(hgap=4,  # 控件之间的相邻两行之间的像素数量
                                vgap=4)  # 控件的相邻两列之间的像素数量
        for col in range(3):
            for row in range(3):
                btn = wx.Button(panel, -1, str(row) + str(col))
                sizer.Add(btn, pos=(row, col))

        bt1 = wx.Button(panel, -1, "Shell")
        bt2 = wx.Button(panel, -1, "Python")
        sizer.Add(window=bt1,
                  pos=(0, 3),  # 指定子部件所在的位置，这里是在第1行的第4列添加
                  span=(3, 1),  # 指定跨越的行和列数
                  flag=wx.EXPAND)  # 设置显示格式
        sizer.Add(bt2, (3, 0), (1, 4), wx.EXPAND)

        sizer.AddGrowableCol(3)  # 扩展指定的列
        sizer.AddGrowableRow(3)  # 扩展指定的行

        panel.SetSizer(sizer)
        panel.Fit()


if __name__ == '__main__':
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()

# ### wx.GridSizer
# https://docs.wxpython.org/wx.GridSizer.html
# 严格遵循网格，均匀排布，适用于处理一些基于表格的信息；
#
# ### wx.FlexGridSizer
# https://docs.wxpython.org/wx.FlexGridSizer.html
# 相比wx.GridSizer灵活：
# - 可以单独设置每行每列的尺寸，
# - 默认单元格的尺寸不随着窗口尺寸改变而变化等；
# - 可以通过AddGroveableCol()和AddGrowableRow()方法扩展指定的列或行；
#
# ### wx.GridBagSizer
# https://docs.wxpython.org/wx.GridBagSizer.html
# 对FlexGridSizer的进一步增强：
# - 可以将一个子部件添加到一个特定的单元格；
# - 可以将一个窗口部件跨越几个单元格；
