# coding=utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox as msg
from tkinter import Spinbox
import ZToolTip as tt

GLOBAL_CONST = 123


class OOP():
    def __init__(self):  # Initializer method
        self.win = tk.Tk()
        tt.create_ToolTip(self.win, 'Hello GUI')
        self.win.title("Python GUI")
        self.win.iconbitmap('ZTemp.ico')
        self.create_widgets()

    def click_me(self):
        self.action.configure(text='Hello ' + self.name.get() + ' ' + self.number_chosen.get())

    def _spin(self):
        value = self.spin.get()
        print(value)
        self.scrol.insert(tk.INSERT, value + '\n')

    def rad_call(self):
        radSel = self.radVar.get()
        if radSel == 0:
            self.mighty2.configure(text='Blue')
        elif radSel == 1:
            self.mighty2.configure(text='Gold')
        elif radSel == 2:
            self.mighty2.configure(text='Red')

    @staticmethod
    def using_global():
        global GLOBAL_CONST
        print(GLOBAL_CONST)
        GLOBAL_CONST = 789
        print(GLOBAL_CONST)

    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit()

    def create_widgets(self):
        tab_control = ttk.Notebook(self.win)
        tab1 = ttk.Frame(tab_control)
        tab_control.add(tab1, text='Tab 1')
        tab2 = ttk.Frame(tab_control)
        tab_control.add(tab2, text='Tab 2')
        tab_control.pack(expand=1, fill="both")

        mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
        mighty.grid(column=0, row=0, padx=8, pady=4)

        a_label = ttk.Label(mighty, text="Enter a name:")
        a_label.grid(column=0, row=0, sticky='W')
        ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)

        self.name = tk.StringVar()
        self.name_entered = ttk.Entry(mighty, width=12, textvariable=self.name)
        self.name_entered.grid(column=0, row=1, sticky='W')
        self.name_entered.focus()

        self.action = ttk.Button(mighty, text="Click Me!", command=self.click_me)
        self.action.grid(column=2, row=1)

        number = tk.StringVar()
        self.number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
        self.number_chosen['values'] = (1, 2, 4, 42, 100)
        self.number_chosen.grid(column=1, row=1)
        self.number_chosen.current(0)

        self.spin = Spinbox(mighty, values=(1, 2, 4, 42, 100), width=5, bd=9, command=self._spin)
        self.spin.grid(column=0, row=2)

        scrol_w, scrol_h = 30, 8
        self.scrol = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
        self.scrol.grid(column=0, row=3, sticky='WE', columnspan=3)

        for child in mighty.winfo_children():
            child.grid_configure(padx=4, pady=2)

        self.mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.mighty2.grid(column=0, row=0, padx=8, pady=4)

        colors = ["Blue", "Gold", "Red"]

        self.radVar = tk.IntVar()
        self.radVar.set(99)
        for col in range(3):
            cur_rad = tk.Radiobutton(self.mighty2, text=colors[col], variable=self.radVar, value=col,
                                     command=self.rad_call)
            cur_rad.grid(column=col, row=1, sticky=tk.W)
            tt.create_ToolTip(cur_rad, 'This is a Radiobutton control')

        for child in self.mighty2.winfo_children():
            child.grid_configure(padx=8, pady=2)

        menu_bar = Menu(self.win)
        self.win.config(menu=menu_bar)
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="New")
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self._quit)
        menu_bar.add_cascade(label="File", menu=file_menu)

        def _msgBox():
            msg.showinfo('Python Message Info Box', 'Message:\nTest!.')

        help_menu = Menu(menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=_msgBox)
        menu_bar.add_cascade(label="Help", menu=help_menu)

        self.using_global()

        # Add Tooltips to widgets
        tt.create_ToolTip(self.spin, 'This is a Spinbox control')
        tt.create_ToolTip(self.name_entered, 'This is an Entry control')
        tt.create_ToolTip(self.action, 'This is a Button control')
        tt.create_ToolTip(self.scrol, 'This is a ScrolledText control')


oop = OOP()
oop.win.mainloop()
