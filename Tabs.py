from tkinter import *
from tkinter import ttk


window = Tk()

notebook = ttk.Notebook(window) # widget that manages a collection of windows/displays
tab1 = Frame(notebook) # new frame for tab1
tab2 = Frame(notebook) # new frame for tab1

notebook.add(tab1, text = "Opcje 1")
notebook.add(tab2, text = "Opcje 2")

notebook.pack(expand=True, fill="both")

Label(tab1, text="Hello, this is tab 1", width=50, height=25).pack()
Label(tab2, text="Goodbye, this is tab 1", width=50, height=25).pack()
window.mainloop()

