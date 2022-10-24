from tkinter import *
STEP = 10

def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-STEP)

def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+STEP)

def move_left(event):
    label.place(x=label.winfo_x()-STEP, y=label.winfo_y())

def move_right(event):
    label.place(x=label.winfo_x()+STEP, y=label.winfo_y())


window = Tk()
window.geometry("500x500")

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

window.bind("<Up>", move_up)
window.bind("<Down>", move_down)
window.bind("<Left>", move_left)
window.bind("<Right>", move_right)


myimage = PhotoImage(file="images/pythonLogo.png")
label = Label(window, image=myimage)
label.place(x=0, y=0)
window.mainloop()