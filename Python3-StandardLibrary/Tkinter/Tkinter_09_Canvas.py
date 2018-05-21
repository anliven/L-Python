#! python3
# -*- coding: utf-8 -*-
import os
from time import sleep
import tkinter
import tkinter.filedialog
import tkinter.messagebox
from PIL import ImageGrab, Image

root = tkinter.Tk()
root.title("Tkinter08 Demo")
root.geometry('200x120+400+300')  # 设置窗口大小与位置，“width x height + xoffset + yoffset”
# root.resizable(False, False)  # 设置窗口大小不可改变


class MyCapture:

    def __init__(self, png):
        self.X = tkinter.IntVar(value=0)  # 记录鼠标左键按下的位置
        self.Y = tkinter.IntVar(value=0)
        screen_width = root.winfo_screenwidth()  # 屏幕尺寸
        screen_height = root.winfo_screenheight()
        self.top = tkinter.Toplevel(root, width=screen_width, height=screen_height)  # 创建顶级组件容器
        self.top.overrideredirect(True)  # 不显示最大化、最小化按钮
        self.image = tkinter.PhotoImage(file=png)
        self.canvas = tkinter.Canvas(self.top, bg='white', width=screen_width, height=screen_height)  # 创建画布
        self.canvas.create_image(screen_width // 2, screen_height // 2, image=self.image)  # 显示全屏截图，并进行区域截图

        def onLeftButtonUp(event):  # 获取鼠标左键抬起的位置并取色
            im = Image.open(png)
            color = im.getpixel((event.x, event.y))[:3]
            color = map(lambda x: hex(x)[2:], color)
            color = map(lambda x: x if len(x) == 2 else '0' + x, color)
            color = '#' + ''.join(color)
            tkinter.messagebox.showinfo('', str(color))
            self.top.destroy()  # 关闭当前窗口

        self.canvas.bind('<ButtonRelease-1>', onLeftButtonUp)
        self.canvas.pack(fill=tkinter.BOTH, expand=tkinter.YES)  # 画布充满窗口，并随窗口自动适应大小


def buttonCaptureClick():  # 截图
    root.state('icon')  # 最小化主窗口
    sleep(0.2)
    filename = 'temp.png'
    im = ImageGrab.grab()  # 默认对全屏幕进行截图
    im.save(filename)
    im.close()
    w = MyCapture(filename)
    buttonCapture.wait_window(w.top)  # 显示全屏幕截图
    root.state('normal')  # 截图结束，恢复主窗口，并
    os.remove(filename)  # 删除临时的全屏幕截图文件


buttonCapture = tkinter.Button(root, text='取色', command=buttonCaptureClick)
buttonCapture.place(x=10, y=10, width=80, height=20)

root.mainloop()

# ### 窗口美化
# title()/wm_title() ：窗口标题；
# geometry() ：窗口大小；
# overrideredirect() ：去除边框；
# iconbitmap()/wm_iconbitmap() ：标题栏图标；
#
# ### 画布（Canvas）
# 用于绘制图形；
