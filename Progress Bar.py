from tkinter import *
from tkinter.ttk import *
import time
from random import *

def start():
    gb = 100
    download = 0
    speed = 1
    while download < gb:
        time.sleep(0.05)
        speed = randrange(-2, 3)
        bar['value'] += 100 * speed/gb
        download += speed
        percent.set(str(int(100 * download/gb)) + "%")
        text.set(str(download) + "/"+str(gb) + " GBs completed.")
        window.update_idletasks()



window = Tk()

percent = StringVar()
text = StringVar()
percentLabel = Label(window, textvariable=percent).pack()
taskLabel = Label(window, textvariable=text).pack()


bar = Progressbar(window, orient=HORIZONTAL, length = 300)
bar.pack(pady=10)
button=Button(window, text="download", command=start).pack()

window.mainloop()