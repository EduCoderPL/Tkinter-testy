from tkinter import *
def submit():
    print(f"Temperatura wynosi: {scale.get()} stopni Celcjusza.")

window = Tk()

scale = Scale(window,
              from_=100,
              to=0,
              length = 600,
              orient=VERTICAL,
              font = ("Consolas", 20),
              tickinterval = 20,
              showvalue = 1,
              resolution = 5,
              troughcolor = "#69EAFF",
              fg = "#FF1C00",
              bg = "#111111"

              )

scale.set(100)
scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()