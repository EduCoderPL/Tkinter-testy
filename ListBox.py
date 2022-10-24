from tkinter import *

def submit():
    if listbox.curselection():
        languages = []
        for index in listbox.curselection():
            languages.insert(index, listbox.get(index))
        print("Wybrałeś język: ")
        for language in languages:
            print(language)
def add():
    if entryBox.get():
        listbox.insert(listbox.size(), entryBox.get())
        listbox.config(height=listbox.size())


def delete():
    for item in reversed(listbox.curselection()):
        listbox.delete(item)
    listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg = "#CCCCCC",
                  font=("Constantia", 35),
                  width=12)
listbox.pack()

listbox.insert(1, "Python")
listbox.insert(2, "Java")
listbox.insert(3, "C++")
listbox.insert(4, "C#")
listbox.insert(5, "HTML")
listbox.insert(6, "Javascript")

listbox.config(height=listbox.size())

entryBox = Entry(window)
entryBox.pack()


submitButton = Button(window, text="Submit", command=submit)
submitButton.pack()

addButton = Button(window, text="Add", command=add)
addButton.pack()

deleteButton = Button(window, text="Delete", command=delete)
deleteButton.pack()




window.mainloop()

