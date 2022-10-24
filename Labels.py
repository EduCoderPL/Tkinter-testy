from tkinter import *

# Label - zakładka, która przechowuje fragment okienka z tekstami, obrazkami, etc...
window = Tk(className="Generator Memów")
window.geometry("1300x1300")
photo = PhotoImage(file="images/balis.png")


label = Label(window,
              text="Hello World", # Tekst
              font=("Arial", 40, "bold"), # Czcionka
              fg="green", # Kolor tekstu
              bg="black", # Kolor tła
              relief=RAISED, # Styl krawędzi
              bd=10, # Grubość krawędzi
              padx=20, # Wcięcie poziome
              pady=20, # Wcięcie pionowe
              image=photo, # Obrazek
              compound = "top") # Położenie obrazka


# Polecenia dodające label do okienka
label.pack()
# label.place(x=100, y=100)

window.mainloop()
