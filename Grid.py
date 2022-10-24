from tkinter import *

window = Tk()
frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.pack()

titleLabel=Label(frame, text="Enter your info", font=("Arial", 25)).grid(row=0, column=0, columnspan=2)

firstNameLabel = Label(frame, text="First name: ", width=20, bg="red").grid(row=1, column = 0)
firstNameEntry = Entry(frame).grid(row=1, column=1)

lastNameLabel = Label(frame, text="Last name: ",bg="green").grid(row=2, column = 0)
lastNameEntry = Entry(frame).grid(row=2, column=1)

emailLabel = Label(frame, text="e-mail: ",bg="blue", width = 30).grid(row=3, column = 0)
emailEntry = Entry(frame).grid(row=3, column=1)

submitButton = Button(frame, text="Submit").grid(row = 4, column = 0, columnspan=2)



window.mainloop()