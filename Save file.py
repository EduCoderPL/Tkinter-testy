from tkinter import *
from tkinter import filedialog


def saveFile():
    file = filedialog.asksaveasfile(initialdir="./",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Pliki tekstowe", ".txt"),
                                        ("Pliki HTML", ".html"),
                                        ("Wszystkie pliki", ".*")
                                    ])

    if file is None:
        return
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()


window = Tk()
button = Button(text="save", command=saveFile)
button.pack()

text = Text(window)
text.pack()
window.mainloop()
