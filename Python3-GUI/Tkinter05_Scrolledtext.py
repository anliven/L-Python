# coding=utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext  # scrolled text

win = tk.Tk()
win.title("Python GUI")

ttk.Label(win, text="Enter a name:").grid(column=0, row=0)
ttk.Label(win, text="Choose a number:").grid(column=1, row=0)


def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()

action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number, state='readonly')
number_chosen['values'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)

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
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2:
        win.configure(background=colors[2])


# widgets in loop
radVar = tk.IntVar()  # create three Radiobuttons using one variable
radVar.set(99)  # selecting a non-existing index value for radVar
for col in range(3):  # creating all three Radiobutton widgets within one loop
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar, value=col, command=rad_call)
    curRad.grid(column=col, row=5, sticky=tk.W)

# Using a scrolled Text control
scrol_w, scrol_h = 30, 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
# scr.grid(column=0, sticky='WE', columnspan=3)
scr.grid(column=0, columnspan=3)  # sticky property removed

win.mainloop()
