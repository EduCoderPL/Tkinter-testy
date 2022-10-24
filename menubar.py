from tkinter import *


def openFile():
    print("Opened file")

def saveFile():
    print("File has been saved")

def cut():
    print("text cutted")

def copy():
    print("text copied")

def paste():
    print("text pasted")




window = Tk()
openImage = PhotoImage(file="images/load.png")
saveImage = PhotoImage(file="images/load.png")
menubar = Menu(window)
window.config(menu=menubar)

fileMenu = Menu(menubar, tearoff=0, font=("MV Boli", 12))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile, image = openImage, compound="left")
fileMenu.add_command(label="Save", command=saveFile, image = saveImage, compound="left")
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()