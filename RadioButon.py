from tkinter import *

food = ["GDevelop", "Unity", "Construct"]
logoFiles = ("images/GDevelop.png", "images/Unity.png", "images/Construct.png")

def order():
    if x.get() == 0:
        print("You chose GDevelop!")
    elif x.get() == 1:
        print("You chose Unity!")
    elif x.get() == 2:
        print("You are so rich and use Construct")
    else:
        print("Excuse me, what the fuck?!")


window = Tk()

gameEngineImages = [PhotoImage(file=path) for path in logoFiles]
x = IntVar()

for index, element in enumerate(gameEngineImages):
    radiobutton = Radiobutton(window,
                              text=food[index],
                              variable=x,
                              value=index, # Przydziela numerki przyciskom)
                              padx = 25,
                              font=("Impact", 20),
                              image = gameEngineImages[index],
                              compound="left",
                              indicatoron=0,
                              width = 375,
                              command = order)


    radiobutton.pack(anchor=W)

window.mainloop()