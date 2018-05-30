# -*- coding: utf-8 -*-
import tkinter
import tkinter.messagebox
import tkinter.filedialog
import os

filename = ''


def author():
    tkinter.messagebox.showinfo('Author:', 'Tester')


def about():
    tkinter.messagebox.showinfo('License:', 'None.')


def open_file(event=""):
    global filename
    filename = tkinter.filedialog.askopenfilename(defaultextension='.txt')
    if filename == '':
        filename = None
    else:
        root.title('File Name : ' + os.path.basename(filename))
        textPad.delete(1.0, "end")
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()


def new_file(event=""):
    global root, filename, textPad
    root.title('File Name : ' + '未命名.txt')
    filename = "未命名.txt"
    textPad.delete(1.0, "end")


def save_file(event=""):
    global filename
    if filename is None:
        filename = "未命名.txt"
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, "end")
        f.write(msg)
        f.close()
    except IOError:
        save_as_file()


def save_as_file(event=""):
    global filename
    try:
        f = tkinter.filedialog.asksaveasfilename(initialfile='未命名.txt', defaultextension='.txt')
        filename = f
        fh = open(f, 'w')
        msg = textPad.get(1.0, "end")
        fh.write(msg)
        fh.close()
    except IOError:
        pass
    textPad.delete(1.0, "end")


def cut_text():
    global textPad
    textPad.event_generate('<<Cut>>')


def copy_text():
    global textPad
    textPad.event_generate('<<Copy>>')


def paste_text():
    global textPad
    textPad.event_generate('<<Paste>>')


def redo_text():
    global textPad
    textPad.event_generate('<<Redo>>')


def undo_text():
    global textPad
    textPad.event_generate('<<Undo>>')


def select_all_text(event=""):
    global textPad
    textPad.tag_add('sel', '1.0', "end")


def popup(event):
    global edit_menu
    edit_menu.tk_popup(event.x_root, event.y_root)


# 创建界面
root = tkinter.Tk()
root.title('Tkinter12 Demo')
root.geometry("500x500+100+100")
menu_bar = tkinter.Menu(root)
# 文件菜单
file_menu = tkinter.Menu(menu_bar)
file_menu.add_command(label='新建', accelerator='Ctrl+N', command=new_file)  # accelerator属性：显示快捷键信息
file_menu.add_command(label='打开', accelerator='Ctrl+O', command=open_file)
file_menu.add_command(label='保存', accelerator='Ctrl+S', command=save_file)
file_menu.add_command(label='另存为', accelerator='Ctrl+Alt+S', command=save_as_file)
menu_bar.add_cascade(label='文件', menu=file_menu)
# 编辑菜单
edit_menu = tkinter.Menu(menu_bar)
edit_menu.add_command(label='撤销', accelerator='Ctrl+Z', command=undo_text)
edit_menu.add_command(label='重做', accelerator='Ctrl+Y', command=redo_text)
edit_menu.add_separator()
edit_menu.add_command(label='剪切', accelerator='Ctrl+X', command=cut_text)
edit_menu.add_command(label='复制', accelerator='Ctrl+C', command=copy_text)
edit_menu.add_command(label='粘贴', accelerator='Ctrl+V', command=paste_text)
edit_menu.add_separator()
edit_menu.add_command(label='全选', accelerator='Ctrl+A', command=select_all_text)
menu_bar.add_cascade(label='编辑', menu=edit_menu)
# 关于菜单
about_menu = tkinter.Menu(menu_bar)
about_menu.add_command(label='作者', command=author)
about_menu.add_command(label='版权', command=about)
menu_bar.add_cascade(label='关于', menu=about_menu)
# 指定顶层菜单
root.config(menu=menu_bar)

# 工具栏
shortcut_bar = tkinter.Frame(root, height=25, bg='Light sea green')
shortcut_bar.pack(expand="no", fill="x")
in_label = tkinter.Label(root, width=2, bg='antique white')
in_label.pack(side="left", anchor='nw', fill="y")

textPad = tkinter.Text(root, undo=True)
textPad.pack(expand="yes", fill="both")
scroll = tkinter.Scrollbar(textPad)
scroll.config(command=textPad.yview)
scroll.pack(side="right", fill="y")
textPad.config(yscrollcommand=scroll.set)

# 通过键位绑定实现快捷键功能
root.bind("<Control-n>", new_file)
root.bind("<Control-o>", open_file)
root.bind("<Control-s>", save_file)
root.bind("<Control-Alt-s>", save_as_file)
root.bind("<Control-a>", select_all_text)
root.bind("<Button-3>", popup)

# 主消息循环
root.mainloop()


# ### 文件对话框（filedialog）
# 具体信息可查看源码文件（“Python安装目录\Lib\tkinter\filedialog.py”）；
