from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock")


label = Label(root,font=("arial",80),background="black",foreground="purple")
label.pack(anchor="center")

def getTime():
    t = strftime("%H : %M : %S - %p")
    label.config(text=t)

    label.after(1000,getTime)
getTime()
root.mainloop()