# coding=utf-8
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu  # Menu

win = tk.Tk()
win.title("Python GUI")

tabControl = ttk.Notebook(win)  # Create Tab Control
tab1 = ttk.Frame(tabControl)  # Create a tab
tabControl.add(tab1, text='Tab 1')  # Add the tab
tab2 = ttk.Frame(tabControl)  # Add a second tab
tabControl.add(tab2, text='Tab 2')  # Make second tab visible
tabControl.pack(expand=1, fill="both")  # Pack to make visible

mighty = ttk.LabelFrame(tab1, text=' Mighty Python ')  # creating a container frame
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

scrol_w, scrol_h = 30, 3
scr = scrolledtext.ScrolledText(mighty, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, row=2, sticky='WE', columnspan=3)

mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')  # creating a container frame
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


# Exit GUI cleanly
def _quit():
    win.quit()
    win.destroy()
    exit()


# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Add menu items
file_menu = Menu(menu_bar, tearoff=0)  # create File menu
file_menu.add_command(label="New")  # add File menu item
file_menu.add_separator()  # add a separator
file_menu.add_command(label="Exit", command=_quit)
menu_bar.add_cascade(label="File", menu=file_menu)  # add File menu to menu bar and give it a label
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About")

win.mainloop()
