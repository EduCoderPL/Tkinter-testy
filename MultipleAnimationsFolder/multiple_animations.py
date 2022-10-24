from tkinter import *
import time
from Ball import *
import random

window = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()
balls = []

for i in range(1):
    randDiameter = random.randint(0, 100)
    randX = random.randint(randDiameter, WIDTH - randDiameter)
    randY = random.randint(randDiameter, HEIGHT - randDiameter)
    randVelX = random.randint(-4, 4)
    randVelY = random.randint(-4, 4)
    randomColor = random.choice(("white", "red", "blue", "black", "grey", "green", "pink"))

    newBall = Ball(canvas, randX, randY, randDiameter, randVelX, randVelY, "white")
    balls.append(newBall)
    print(newBall.image.)

while True:
    for ball in balls:
        ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()