import tkinter
from tkinter import *
import tkinter.messagebox
top=tkinter.Tk()
r1=IntVar()
c1=IntVar()
c2=IntVar()
c3=IntVar()

l1=Label(top,text="Firstname")
l2=Label(top,text="Lastname")
l3=Label(top,text="Age")
l1.grid(row=0,column=0)
l2.grid(row=1,column=0)
l3.grid(row=2,column=0)
e1=Entry(top,bd=5)
e2=Entry(top,bd=5)
e3=Entry(top,bd=5)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)
e3.grid(row=2,column=1)

l4=Label(top,text="Gender")
l4.grid(row=4,column=0)
rb1=Radiobutton(top,text="Male",variable=r1,value=1)
rb2=Radiobutton(top,text="Female",variable=r1,value=2)
rb1.grid(row=4,column=1)
rb2.grid(row=4,column=2)

l5=Label(top,text="Education")
l5.grid(row=5,column=0)
cb1=Checkbutton(top,text="12th",variable="c1",onvalue=1,offvalue=0)
cb2=Checkbutton(top,text="Btech",variable="c2",onvalue=1,offvalue=0)
cb3=Checkbutton(top,text="Mtech",variable="c3",onvalue=1,offvalue=0)
cb1.grid(row=5,column=1)
cb2.grid(row=5,column=2)
cb3.grid(row=5,column=3)

def sucess():
    tkinter.messagebox.showinfo("Sucessful Login","Welcome!")
b1=Button(top,text="Submit",command=sucess)
b1.grid(row=6,column=1)

top.mainloop()
