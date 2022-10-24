from tkinter import *
STEP = 10

def move_up(event):
    canvas.move(myimage, 0, -STEP)

def move_down(event):
    canvas.move(myimage, 0, STEP)

def move_left(event):
    canvas.move(myimage, -STEP, 0)

def move_right(event):
    canvas.move(myimage, STEP, 0)

window = Tk()

window.bind("<w>", move_up)
window.bind("<s>", move_down)
window.bind("<a>", move_left)
window.bind("<d>", move_right)

canvas = Canvas(window, width=500, height=500)
canvas.pack()


photoimage = PhotoImage(file="images/pythonLogo.png")
myimage = canvas.create_image(0, 0, image=photoimage)


window.mainloop()