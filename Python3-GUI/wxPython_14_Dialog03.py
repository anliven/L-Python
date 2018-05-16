#! python3
# -*- coding: utf-8 -*-
import wx
import time


def test_pdlg(flag, count):
    dlg = wx.ProgressDialog(title="Dialog03 Demo",
                            message="Time remaining",
                            maximum=150,
                            style=wx.PD_REMAINING_TIME | wx.PD_CAN_ABORT
                            )
    while flag and count < 150:
        count += 10
        wx.Sleep(1)
        flag = dlg.Update(value=count,  # 当前完成的进度数值
                          newmsg=time.ctime())  # 显示最新信息
    dlg.Destroy()


if __name__ == "__main__":
    app = wx.App()
    test_pdlg(True, 30)
    app.MainLoop()

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
