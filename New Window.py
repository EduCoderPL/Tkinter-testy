from tkinter import *

def create_window():
    new_window=Tk()
    # new_window = Toplevel()
    oldWindow.destroy()

oldWindow = Tk()

Button(oldWindow, text="Create new window", command = create_window).pack()

oldWindow.mainloop()