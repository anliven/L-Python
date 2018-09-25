# -*- coding: utf-8 -*-
import wx


class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "Dialog01 Demo", size=(300, 300))
        panel = wx.Panel(self)
        btn1 = wx.Button(panel, -1, "MessageBox", (30, 30))
        btn1.Bind(wx.EVT_BUTTON, self.onClick_MessageBtn)
        btn2 = wx.Button(panel, -1, "GetTextFromUser", (30, 80))
        btn2.Bind(wx.EVT_BUTTON, self.onClick_GetTextFromUser)
        btn3 = wx.Button(panel, -1, "GetSingleChoice", (30, 130))
        btn3.Bind(wx.EVT_BUTTON, self.onClick_GetSingleChoice)
        btn4 = wx.Button(panel, -1, "FileSelector", (30, 180))
        btn4.Bind(wx.EVT_BUTTON, self.onClick_GetFile)

    def onClick_MessageBtn(self, event):
        wx.MessageBox(message="This is a MessageBox.",  # 显示的信息
                      caption="MessageBox",  # 显示的标题
                      style=wx.OK)  # 显示的格式

    def onClick_GetTextFromUser(self, event):
        name = wx.GetTextFromUser(message="Input your name : ",
                                  caption="GetTextFromUser")
        print("Your name is", name)

    def onClick_GetSingleChoice(self, event):
        code = ["Python", "Shell", "Java"]
        choice = wx.GetSingleChoice(message="Which do you like best ?",
                                    caption="GetSingleChoice",
                                    aChoices=code)  # 可选择的列表
        if choice is "":
            print("Nothing.")
        else:
            print("Your choice is", choice)

    def onClick_GetFile(self, event):
        filename = wx.FileSelector("Choose a file to open")
        if filename.strip():
            print("File: ", filename)


if __name__ == "__main__":
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()

# ### 全局函数
# https://docs.wxpython.org/wx.functions.html
# 使用全局函数，可以避免进行类的实例化等繁琐的过程；
#
# ### 信息框（全局函数wx.MessageBox）
# 用于显示信息；
# https://docs.wxpython.org/wx.functions.html#wx.MessageBox
# 使用全局函数wx.MessageBox可以方便地创建信息框；
#
# ### 文本对话框
# 用于获取用户输入的文本信息；
# - 获取文本信息：https://docs.wxpython.org/wx.functions.html#wx.GetTextFromUser
# - 获取密码：https://docs.wxpython.org/wx.functions.html#wx.GetPasswordFromUser
# - 获取数字信息：https://docs.wxpython.org/wx.functions.html#wx.GetNumberFromUser
#
# ### 列表项对话框（全局函数wx.GetSingleChoice）
# 对话框显示一个列表项，用户可以从中选择一个选项；
# https://docs.wxpython.org/wx.functions.html#wx.GetSingleChoice
# 返回值是选项的字符串，如果按下的是Cancel，那么返回值是一个空字符串；
#
# ### 文件对话框（全局函数wx.FileSelector）
# https://docs.wxpython.org/wx.functions.html#wx.FileSelector
