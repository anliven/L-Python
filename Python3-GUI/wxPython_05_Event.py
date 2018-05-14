#! python3
# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Event Demo", wx.DefaultPosition, (300, 300))
        panel = wx.Panel(self)
        test_button = wx.Button(panel,
                                id=-1,
                                label="Click on the button",
                                pos=(60, 150))
        test_button.Bind(wx.EVT_BUTTON, self.onButtonClick, test_button)  # 按钮被按下调用函数
        test_label = wx.StaticText(panel,
                                   id=-1,
                                   label="Click on the static text",
                                   pos=(60, 50))
        test_label.Bind(event=wx.EVT_LEFT_DOWN, handler=self.onTextClick, source=test_label)  # 鼠标左键被按下调用函数

    def onButtonClick(self, event):
        print("# The button is clicked.")

    def onTextClick(self, event):
        print("$ The static text is clicked.")


if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()

# ### 事件（wx.Event类）
# https://docs.wxpython.org/wx.Event.html
# 事件：操作系统接收用户的操作，然后传递信息给应用程序，应用程序执行相应的功能（执行相应的代码）；
#
# ### 一些概念
# - 在wxPython中，所有事件都是wx.Event或其子类的实例，每个事件都有一个事件类型属性，用于区分不同的事件；
# - 事件队列：存放事件信息，先进先出的数据结构，先发生的事件先被处理；
# - 每个事件都应该有相应的事件处理器（通常是一个函数），事件发生时，相应的事件处理器被调用；
# - 如果一个事件没有对应的事件处理器，那么该事件就会被忽略；
# - 使用Bind函数绑定事件和相应事件处理器（建立关联关系）；
#
# ### wx.EvtHandler.Bind方法
# https://docs.wxpython.org/wx.EvtHandler.html#wx.EvtHandler.Bind
# wx.EvtHandler类是所有可显示对象的父类，因此常用的控件包括Frame都可以使用Bind方法；
# 调用格式：
# - Bind(self, event, handler, source=None, id=wx.ID_ANY, id2=wx.ID_ANY)
# - 参数event ：绑定的事件类型，都是以“wx.EVT_”开头的全局变量
# - 参数handler ：事件处理器(事件发生之后的回调函数),注意参数值只是一个函数名
# - 参数source ：事件源对象（事件发生源），用于区分相同类型的事件
# - 参数id、id2 ：用ID来指定事件源；
#                如果只写一个id，那么和source的作用相同；
#                如果写了两个id，则在这两个id之间的数值都被绑定相应的事件，并且调用相同的事件处理函数；
#
# ### 一些事件类型
# - wx.EVT_LEFT_DOWN ：鼠标左键按下
# - wx.EVT_LEFT_UP ：鼠标左键松开
# - wx.EVT_LEFT_DCLICK ：鼠标左键双击
# - wx.EVT_RIGHT_DOWN ：鼠标右键按下
# - wx.EVT_RIGHT_UP ：鼠标右键松开
# - wx.EVT_RIGHT_DCLICK ：鼠标右键双击
# - wx.EVT_MOTION ：鼠标移动
# - wx.EVT_MOUSE_EVENTS ：所有鼠标事件
# - wx.EVT_BUTTON ：按钮被按下
# - wx.EVT_MENU ：菜单项被选择
#
# ### 事件处理机制简介
# 传递机制：
# - 如果一个父对象中包含了子对象，两者都可以响应同一个事件，那么会优先在子对象中响应；
# - 然后判断是否设置了继续传递，如果可以，则父对象中也会响应，否则，父对象无法响应该事件；
# 区分事件类与事件类型：
# - 事件类是一个类，而事件类型则是C++定义的宏，可以当做全局有效的常量；
#
# ### 常见的事件类
# - CloseEvent : 窗口关闭时触发
# - CommandEvent : 与窗口部件的简单交互，例如菜单项选择、按钮被单击
# - KeyEvent : 按键事件
# - MouseEvent : 鼠标事件
# - PaintEvent : 当窗口的内容需要被重绘时触发
# - SizeEvent : 当窗口的大小或布局被改变时触发
