import tkinter
import tkinter.messagebox
top=tkinter.Tk()
def hellocallback():
    tkinter.messagebox.showinfo("hello python","hello world")
B=tkinter.Button(top,text="hello",command=hellocallback)
B.pack()
top.mainloop()
import tkinter
from tkinter import *
import tkinter.messagebox
top=tkinter.Tk()
ck1=IntVar()
ck2=IntVar()
c1=Checkbutton(top,text='music',variable=ck1,onvalue=1,offvalue=0,height=5,width=20)
c2=Checkbutton(top,text='video',variable=ck2,onvalue=1,offvalue=0,height=5,width=20)
c1.pack()
c2.pack()
top.mainloop()
import tkinter
from tkinter import *
top=tkinter.Tk()
l1=Label(top,text="Username")
l2=Label(top,text="")
l3=Label(top,text="Password")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1=Entry(top,bd=5)
e3=Entry(top,bd=5)
e1.grid(row=0,column=1)
e3.grid(row=2,column=1)
top.mainloop()
import tkinter
from tkinter import *
root=tkinter.Tk()
var=IntVar()
def sel():
    selection="selected option"+str(var.get())
    Label.config(text=selection)
r1=Radiobutton(root,text="option1",variable=var,value=1,command=sel)
r1.pack(anchor=W)
r2=Radiobutton(root,text="option2",variable=var,value=2,command=sel)
r2.pack(anchor=W)
r3=Radiobutton(root,text="option3",variable=var,value=3,command=sel)
r3.pack(anchor=W)
label=Label(root)
label=pack()
root.mainloop()
