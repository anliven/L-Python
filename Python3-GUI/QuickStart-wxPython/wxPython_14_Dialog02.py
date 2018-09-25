# -*- coding: utf-8 -*-
import wx
import os
import time


class MyDialog(wx.Dialog):
    def __init__(self, parent, title):
        super(MyDialog, self).__init__(parent, title=title, size=(250, 150))
        panel = wx.Panel(self)
        self.ok_btn = wx.Button(panel, wx.ID_OK, label="OK", size=(50, 20), pos=(30, 30))
        self.ok_btn.SetDefault()
        self.cancel_btn = wx.Button(panel, wx.ID_CANCEL, "Cancel", size=(50, 20), pos=(90, 30))


class MyFrame(wx.Frame):

    def __init__(self, parent, title):
        super(MyFrame, self).__init__(parent, title=title, size=(300, 250))
        self.InitUI()

    def InitUI(self):
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, label="Modal Dialog", pos=(60, 10))
        btn1.Bind(wx.EVT_BUTTON, self.OnModal)
        btn2 = wx.Button(panel, label="Enter Text", pos=(60, 50))
        btn2.Bind(wx.EVT_BUTTON, self.OnTextEntry)
        btn3 = wx.Button(panel, label="Open File", pos=(60, 90))
        btn3.Bind(wx.EVT_BUTTON, self.OnOpenFile)
        btn4 = wx.Button(panel, label="Progress Dialog", pos=(60, 130))
        btn4.Bind(wx.EVT_BUTTON, self.OnProgress)
        self.Centre()
        self.Show(True)

    def OnModal(self, event):
        dlg = MyDialog(self, "Are you OK?")
        result = dlg.ShowModal()  # ShowModal()以模态对话框的方式显示
        if result == wx.ID_OK:
            print("I'm OK!")
        elif result == wx.ID_CANCEL:
            print("I'm so tired.")
        dlg.Destroy()  # 对话框的使用完成后，Destroy()显式地销毁

    def OnTextEntry(self, event):
        dlg = wx.TextEntryDialog(self, 'Enter Your Name', 'TextEntryDialog')
        if dlg.ShowModal() == wx.ID_OK:
            print("Name :" + dlg.GetValue())  # GetValue()返回该文本对话框的内容
        dlg.Destroy()

    def OnOpenFile(self, event):
        wildcard = "Python Files (*.py)|*.py"  # 滤波器
        dlg = wx.FileDialog(parent=self,
                            message="Choose a file",
                            defaultDir=os.getcwd(),
                            defaultFile="",
                            wildcard=wildcard,
                            style=wx.FD_OPEN)
        if dlg.ShowModal() == wx.ID_OK:
            print("File : " + dlg.GetPath())  # GetPath()返回选定文件的完整路径
        dlg.Destroy()

    def OnProgress(self, event):
        flag = True
        count = 0
        dlg = wx.ProgressDialog(parent=self,
                                title="ProgressDialog",
                                message="Time remaining",
                                maximum=120,
                                style=wx.PD_REMAINING_TIME | wx.PD_CAN_ABORT
                                )
        while flag and count < 120:
            count += 10
            wx.Sleep(1)
            flag = dlg.Update(value=count,  # 当前完成的进度数值
                              newmsg=time.ctime())  # 显示最新信息
        dlg.Destroy()


if __name__ == "__main__":
    app = wx.App()
    MyFrame(None, 'Dialog02 Demo')
    app.MainLoop()

# ### 对话框（wx.Dialog类）
# https://docs.wxpython.org/wx.Dialog.html
# 对话框主要可以分为模态对话框和非模态对话框；
# 模态对话框会阻塞其它窗口部件接收用户事件；
# 也就是说，模态对话框一旦被创建，将会一直和该对话框交互，直到该对话框被关闭；
#
# ### 文本对话框（wx.TextEntryDialog类）
# https://docs.wxpython.org/wx.TextEntryDialog.html
#
# ### 文件选择对话框（wx.FileDialog类）
# https://docs.wxpython.org/wx.FileDialog.html
#
# ### 进度条对话框（wx.ProgressDialog类）
# https://docs.wxpython.org/wx.ProgressDialog.html
# 用来指示任务完成的进度；
# 显示格式：
# - wx.PD_APP_MODAL ： 设置整个应用程序为模式状态
# - wx.PD_AUTO_HIDE ： 进度条自动隐藏，直到达到最大值
# - wx.PD_CAN_ABORT ：设置Cancel按钮
# - wx.PD_ELAPSED_TIME ： 显示该对话框已经出现的事件
# - wx.PD_ESTIMATED_TIME : 根据目前进度计算完成的总时间
# - wx.PD_REMAINING_TIME ：完成进度的剩余时间
#
# ### 建议使用全局函数
# https://docs.wxpython.org/wx.functions.html
# 如果全局函数满足需求，建议使用，可以避免进行类的实例化等繁琐的过程；
