from tkinter import *
count=0
def click():
    global count
    count +=1
    print(f"Klikłeś {count} razy.")
    button.config(text = f"Klikaj!!!\n" + f"Klikłeś {count} razy.")



# Button - Przycisk, który po kliknięciu robi rzeczy
window = Tk()
photo=PhotoImage(file="images/testButton.png", )

button = Button(window,
                text="Klikaj!!!\n" + f"Klikłeś {count} razy.",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00DD00",
                activebackground="#393939", #
                state=ACTIVE, # ACTIVE, DISABLED - czy przycisk jest aktywny, czy nie
                image=photo,
                compound="top"
                )


button.pack()

button.place(x=100, y=100)
button.size(x=200, y = 300)

window.mainloop()
