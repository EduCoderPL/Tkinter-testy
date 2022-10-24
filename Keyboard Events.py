from tkinter import *

def doSomething(event):
    print("You pressed: " + event.keysym)
    label.config(text=event.keysym)

window = Tk()
frame = Frame(window, bg="pink", bd=5, relief=SUNKEN, width = 100)
frame.pack()
window.bind("<Key>", doSomething)

label = Label(frame, font=("Helvetica", 48), width = 5)
label.pack()

window.mainloop()