from tkinter import *
from time import *

def update():
    timeString = strftime("%I:%M:%S %p")
    timeLabel.config(text=timeString)

    dayString=strftime(strftime("%A"))
    dayLabel.config(text=dayString)
    timeLabel.after(1000, update)

window = Tk()

timeLabel=Label(window, font=("Arial", 50),
                 fg = "#00FF00",
                 bg="black")

dayLabel = Label(window, font=("Ink Free", 25),)

timeLabel.pack()
dayLabel.pack()
update()


window.mainloop()