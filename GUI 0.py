import tkinter
from tkinter import *
import tkinter.messagebox
top=tkinter.Tk()

def hello():
    tkinter.messagebox.showinfo("welcome","hello world")
b=tkinter.Button(top,text='Click',command=hello)

b.pack(side=RIGHT)


top.mainloop()
