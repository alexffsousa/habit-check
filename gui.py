import tkinter as tk

window = tk.Tk()


def create_window(bg_color):

    window.title("Habits.")
    window.geometry("800x800")

    icon = tk.PhotoImage(file = "imgs\icon.png")

    window.wm_iconphoto(False, icon)
    window.configure(bg=bg_color)

    create_menubar()

    window.mainloop()


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

