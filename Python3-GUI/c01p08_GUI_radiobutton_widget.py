# coding=utf-8
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)


def click_me():
    action.configure(text='Hello ' + name.get() + ' ' +
                          number_chosen.get())


name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)
name_entered.focus()

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(win, text="Disabled", variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=4, sticky=tk.W)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(win, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=4, sticky=tk.W)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win, text="Enabled", variable=chVarEn)
check3.deselect()
check3.grid(column=2, row=4, sticky=tk.W)


# GUI Callback function
def check_callback(*ignoredArgs):  # only enable one checkbutton
    if chVarUn.get():
        check3.configure(state='disabled')
    else:
        check3.configure(state='normal')
    if chVarEn.get():
        check2.configure(state='disabled')
    else:
        check2.configure(state='normal')


# trace the state of the two checkbuttons
chVarUn.trace('w', lambda unused0, unused1, unused2: check_callback())
chVarEn.trace('w', lambda unused0, unused1, unused2: check_callback())

# Radiobutton Globals
COLOR1, COLOR2, COLOR3 = "Blue", "Gold", "Red"


# Radiobutton Callback
def rad_call():
    radSel = radVar.get()
    if radSel == 1:
        win.configure(background=COLOR1)
    elif radSel == 2:
        win.configure(background=COLOR2)
    elif radSel == 3:
        win.configure(background=COLOR3)


# create three Radio-buttons using one variable
radVar = tk.IntVar()
rad1 = tk.Radiobutton(win, text=COLOR1, variable=radVar, value=1, command=rad_call)
rad1.grid(column=0, row=5, sticky=tk.W, columnspan=3)
rad2 = tk.Radiobutton(win, text=COLOR2, variable=radVar, value=2, command=rad_call)
rad2.grid(column=1, row=5, sticky=tk.W, columnspan=3)
rad3 = tk.Radiobutton(win, text=COLOR3, variable=radVar, value=3, command=rad_call)
rad3.grid(column=2, row=5, sticky=tk.W, columnspan=3)

win.mainloop()
