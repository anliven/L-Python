from tkinter import *
from tkinter.ttk import *
import sqlite3 as sql
import os.path as op


class PhoneNote:
    def __init__(self):
        self.root = Tk()
        self.root.title("Tkinter11 Demo")
        self.root.geometry("300x350+400+100")

        self.name_label = Label(self.root, text="姓名：")
        self.name_entry = Entry(self.root)
        self.info_label = Label(self.root, text="信息：")
        self.info_entry = Entry(self.root)
        self.add_btn = Button(self.root, text="添加记录", command=self.add_item)
        self.flush_btn = Button(self.root, text="刷新记录", command=self.view_msg)
        self.msg_label = Label(self.root, text="")

        self.tree = Treeview(self.root, show="headings")
        self.tree["columns"] = ("姓名", "信息")
        self.tree.column("姓名", width=100, anchor='center')
        self.tree.column("信息", width=150, anchor='center')
        self.tree.heading("姓名", text="姓名-Name")
        self.tree.heading("信息", text="信息-Information")

        self.ysb = Scrollbar(self.root, orient="vertical", command=self.tree.yview)  # 垂直滚动条
        self.tree.configure(yscroll=self.ysb.set)  # 滚动条关联

        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.info_label.grid(row=1, column=0)
        self.info_entry.grid(row=1, column=1)
        self.add_btn.grid(row=2, column=0)
        self.flush_btn.grid(row=2, column=1, sticky="e")
        self.msg_label.grid(row=3, column=0, columnspan=3)
        self.tree.grid(row=4, column=0, columnspan=3)
        self.ysb.grid(row=4, column=3, sticky=NS)

        if not op.exists("Tkinter_11.db"):
            self.create_table()
        self.view_msg()
        self.root.mainloop()

    def create_table(self):
        conn = sql.connect("Tkinter_11.db")
        c = conn.cursor()
        c.execute("CREATE TABLE con(conid INTEGER PRIMARY KEY AUTOINCREMENT,name STRING,num STRING)")
        c.close()

    def view_msg(self):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)
        conn = sql.connect("Tkinter_11.db")
        c = conn.cursor()
        msg = c.execute("SELECT * FROM con ORDER BY name")
        for row in msg:
            self.tree.insert("", 0, values=(str(row[1]), str(row[2])))
        c.close()

    def add_item(self):
        name = self.name_entry.get()
        info = self.info_entry.get()
        if name == "" or info == "":
            self.msg_label["text"] = "请填写姓名和信息!"
            return 0
        conn = sql.connect("Tkinter_11.db")
        c = conn.cursor()
        c.execute("INSERT INTO con values(NULL,?,?)", (name, info))
        conn.commit()
        c.close()
        self.name_entry.delete(0, END)
        self.info_entry.delete(0, END)
        self.view_msg()


pn = PhoneNote()

# ### 树形视图（Treeview）
# 具体信息可查看源码文件__init__.py中的Treeview类（“Python安装目录\Lib\tkinter\__init__.py”）；
#
# ### 滚动条（Scrollbar）
# 具体信息可查看源码文件__init__.py中的Scrollbar类（“Python安装目录\Lib\tkinter\__init__.py”）；
