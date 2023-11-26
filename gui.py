import time
import tkinter as tk
from functions import *
import time


window = tk.Tk()


def donothing():
   x = 0


def create_menubar():
    menubar = tk.Menu(window)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=donothing)
    filemenu.add_command(label="Open", command=donothing)
    filemenu.add_command(label="Save", command=donothing)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Help Index", command=donothing)
    helpmenu.add_command(label="About...", command=donothing)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)


def show_habits(habits, backg):
    day = time.ctime()



    window.columnconfigure(0, weight=1)
    window.columnconfigure(1, weight=1)
    window.columnconfigure(2, weight=1)
    window.columnconfigure(3, weight=1)

    day_label = tk.Label(window, text=day, background='red', justify='left', font='Helvetica', height=4)
    day_label.grid(column=0, row=0, ipady=20, columnspan=3)

    tk.Button(window, text='Add new habit', width=15, padx=0,).grid(column=3, row=0)
    tk.Button(window, text=habits[0], width=15, padx=0).grid(column=0, row=1)
    tk.Button(window, text=habits[1], width=15, padx=0).grid(column=1, row=1)
    tk.Button(window, text=habits[2], width=15, padx=0).grid(column=2, row=1)
    tk.Button(window, text=habits[3], width=15, padx=0).grid(column=3, row=1)


def create_window(bg_color, habits_list):

    window.title("Habits.")
    window.geometry("800x800")

    icon = tk.PhotoImage(file = "imgs\icon.png")

    window.wm_iconphoto(False, icon)
    window.configure(bg=bg_color)

    create_menubar()
    show_habits(habits_list, bg_color)
    window.mainloop()
