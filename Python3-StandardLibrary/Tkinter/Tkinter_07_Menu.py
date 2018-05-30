# -*- coding: utf-8 -*-
import tkinter

root = tkinter.Tk()
root.wm_title("Tkinter07 Demo")
root.minsize(300, 100)


def onMenu():
    print("Hi，menu.")


def onTesting():
    print("This is a test.")


menu = tkinter.Menu(root)  # 新建菜单

file_menu = tkinter.Menu(menu, tearoff=0)  # 新建下拉菜单
for item in ["新建", "打开", "保存", "另存为"]:
    file_menu.add_command(label=item, command=onMenu)  # add_command()方法添加菜单项
edit_menu = tkinter.Menu(menu, tearoff=0)
for item in ["复制", "粘贴", "剪切"]:
    edit_menu.add_radiobutton(label=item, command=onMenu)  # add_radiobutton()方法添加单选菜单
view_menu = tkinter.Menu(menu, tearoff=0)
for item in ["默认视图", "新式视图"]:
    view_menu.add_checkbutton(label=item, command=onMenu)  # add_checkbutton()方法添加复选菜单
about_menu = tkinter.Menu(menu, tearoff=0)
about_menu.add_command(label="版权信息", command=onMenu)
about_menu.add_separator()  # 分割线
about_menu.add_command(label="其他说明", command=onMenu)

menu.add_cascade(label="文件", menu=file_menu)  # add_cascade()方法“级联”菜单
menu.add_cascade(label="编辑", menu=edit_menu)
menu.add_cascade(label="视图", menu=view_menu)
menu.add_cascade(label="关于", menu=about_menu)
menu.add_command(label="Testing", command=onTesting)  # 如果在顶层菜单，默认依次向右添加菜单项


def onPop(event):
    menu.post(event.x_root, event.y_root)  # Menu类的post()方法在相应位置弹出菜单


root.bind("<Button-3>", onPop)  # 绑定鼠标右键弹出菜单
root.config(menu=menu)  # 指定顶层菜单
root.mainloop()

# ### 菜单（Menu）
# 具体信息可查看源码文件__init__.py中的Menu类（“Python安装目录\Lib\tkinter\__init__.py”）；
# 一些常用方法：
# - add_command()方法：添加菜单项；
# - add_cascade()方法：“级联”菜单，也就是设置子菜单；
# - post()方法：在相应位置弹出菜单；
# - add_separator()方法：分割线，区分界限；
# - add_radiobutton()方法：单选菜单，只能选定一个；
# - add_checkbutton()方法：复选菜单，可以同时选定多个菜单项；
