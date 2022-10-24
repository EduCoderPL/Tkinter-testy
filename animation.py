from tkinter import *
import time

WIDTH = 500
HEIGHT = 500

xVel = 1
yVel = 1

window = Tk()

canvas = Canvas(window, width = WIDTH, height = HEIGHT)
canvas.pack()

photoImage = PhotoImage(file = "images/pythonLogo.png")
myImage = canvas.create_image(0, 0, image=photoImage, anchor=NW)

imageWidth = photoImage.width()
imageHeight = photoImage.height()

while True:
    coordinates = canvas.coords(myImage)
    print(coordinates)
    canvas.move(myImage, xVel, yVel)
    yVel += 0.1
    if coordinates[1] > HEIGHT:
        yVel *= -1
        canvas.move(myImage, xVel, yVel)
        window.update()


    if coordinates[0] > WIDTH or coordinates[0] < 0:
        xVel *= -1

    window.update()

    time.sleep(0.01)


window.mainloop()