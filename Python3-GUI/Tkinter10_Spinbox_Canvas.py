# coding=utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import messagebox
from tkinter import Spinbox  # Spin box

win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Tab 1')
tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text='Tab 2')
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='Tab 3')
tabControl.pack(expand=1, fill="both")

mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, text="Enter a name:").grid(column=0, row=0, sticky='W')
ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)


def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1, sticky='W')
name_entered.focus()

action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


# Spinbox callback
def _spin():
    value = spin.get()
    print(value)
    scr.insert(tk.INSERT, value + '\n')


# Adding a Spinbox widget
spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8, command=_spin)  # using range
spin.grid(column=0, row=2)
# Adding a second Spinbox
spin2 = Spinbox(mighty, values=(10, 20, 30), width=5, bd=8, relief=tk.RIDGE)  # specify a set of values
# relief value: tk.FLAT/tk.RAISED/tk.SUNKEN(default value)/tk.GROOVE/tk.RIDGE
spin2.grid(column=1, row=2)

scrol_w, scrol_h = 30, 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=3, sticky='WE', columnspan=3)

mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)
chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)
chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)


def check_callback(*ignoredArgs):
    if chVarUn.get():
        check3.configure(state='disabled')
    else:
        check3.configure(state='normal')
    if chVarEn.get():
        check2.configure(state='disabled')
    else:
        check2.configure(state='normal')


chVarUn.trace('w', lambda unused0, unused1, unused2: check_callback())
chVarEn.trace('w', lambda unused0, unused1, unused2: check_callback())

colors = ["Blue", "Gold", "Red"]


def rad_call():
    radSel = radVar.get()
    if radSel == 0:
        mighty2.configure(text='Blue')
    elif radSel == 1:
        mighty2.configure(text='Gold')
    elif radSel == 2:
        mighty2.configure(text='Red')


radVar = tk.IntVar()
radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(mighty2, text=colors[col], variable=radVar, value=col, command=rad_call)
    curRad.grid(column=col, row=6, sticky=tk.W)

buttons_frame = ttk.LabelFrame(mighty2, text=' Labels in a Frame ')
buttons_frame.grid(column=0, row=7)

ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0, sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0, sticky=tk.W)


def _quit():
    win.quit()
    win.destroy()
    exit()


def _msgBox():
    answer = messagebox.askyesnocancel("Python Message Multi Choice Box", "Make the choice:")
    print(answer)
    if answer is True:
        messagebox.showinfo('Message Info Box', 'YES is the Chosen One.')
    elif answer is False:
        messagebox.showwarning('Message Warning Box', 'NO is the chosen One.')
    else:
        messagebox.showerror('Message Error Box', 'Cancel is the chosen One.')


# Tab3
tab3_frame = tk.Frame(tab3, bg='blue')
tab3_frame.pack()
for orange_color in range(2):
    canvas = tk.Canvas(tab3_frame, width=150, height=80, highlightthickness=0, bg='orange')  # Canvas
    canvas.grid(row=orange_color, column=orange_color)

menu_bar = Menu(win)
file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=_msgBox)

win.config(menu=menu_bar)
win.mainloop()
