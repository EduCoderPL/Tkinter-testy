from tkinter import *

window = Tk()
window.geometry("420x420")
window.title("Testowe okienko")

icon = PhotoImage(file="images/LogoFeniks.png")
window.iconphoto(True, icon)
window.config(background="#55543f")


window.mainloop()
