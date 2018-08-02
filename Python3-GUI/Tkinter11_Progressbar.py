# coding=utf-8
import tkinter as tk
from tkinter import ttk
from time import sleep

win = tk.Tk()
win.title("Python GUI")

# Add a Progressbar
progress_bar = ttk.Progressbar(win, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)


# update progressbar in callback loop
def run_probar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i  # increment progressbar
        progress_bar.update()  # have to call update() in loop
    progress_bar["value"] = 0  # reset/clear progressbar


def start_probar():
    progress_bar.start()


def stop_probar():
    progress_bar.stop()


def probar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)


# Create a container to hold buttons
buttons_frame = ttk.LabelFrame(win, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)

# Add Buttons for Progressbar commands
ttk.Button(buttons_frame, text=" Run Progressbar   ", command=run_probar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text=" Start Progressbar  ", command=start_probar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text=" Stop immediately ", command=stop_probar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text=" Stop after second ", command=probar_stop_after).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

win.mainloop()
