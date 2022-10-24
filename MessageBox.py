from tkinter import *
from tkinter import messagebox

def click():
    messagebox.showinfo(title="ACHTUNG!!!", message = "To nie Rickroll")
    messagebox.showerror(title="WARNINg!!!", message="To nie Rickroll")

    if messagebox.askokcancel(title="Ask ok cancel", message = "Czy jesteś tego pewien?"):
        messagebox.showinfo(title="ACHTUNG!!!", message="YOU DID IT")
    else:
        messagebox.showerror(title="WARNINg!!!", message="YOU DID NOT DO IT!!!")

window = Tk()

button = Button(window, command=click, text = "KLIKAJ!!!")
button.pack()

window.mainloop()