#File handling
f=open("pycham.txt","w")
f.write('i am dominic johnson ')
f=open("pycham.txt","a")
f.write('from kottayam')
f=open('pycham.txt','r')
print(f.read())

import os
os.rename('pycham.txt','python.txt')
f=open('pycharm.txt',"x")
f=open('python.txt','r')
c=f.read()
f1=open('pycharm.txt','w')
f1.write(c)
f1=open('pycharm.txt','r')
print(f1.read())
f.close()
f1.close()
f=open('py.txt',"x")
f=open("py.txt",'w')
f.write("do you know me")
f=open('py.txt','r')
a=f.read()
f1=open('pycham.txt','a')
f1.write(a)
f1=open('pycham.txt','r')
print(f1.read())
