from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename(initialdir="D:/Programowanie Projekty",
                                          title= "ODPALAJ!!!",
                                          filetypes=(("Pliki tekstowe", "*.txt"), ("Wszystkie pliki", "*.*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()

window = Tk()
button = Button(text = "Open", command = openFile)
button.pack()
window.mainloop()
