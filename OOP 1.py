#Single inheritace
class Animals:
    def forest(self):
        print("Hi, How are you!")
class cat(Animals):
    def jok(self):
        print("My Name is cat!")
cat().forest()
cat().jok()

#Multiple inheritace        
class car:
    def wheel(self,a,b):
        print(a*b);

class shop(car):
    def stock(self,a,b):
        print(a+b);

class mart(shop):
    def me(self,a,b):
        print(a-b);
        
class bike(shop):
    def b(self,a,b):
       return a/b;

d=bike()
m=mart()
print(d.b(5,10))
shop().wheel(5,10)

#polymor overloading
class maths:
    def sum(self,a=None,b=None,c=None,d=None):
        s=0
        if a!=None and b!=None and c!=None and d!=None:
            s=a*b*c*d
            print(s)
        elif a != None and b!=None and c!=None:
            s=a+b+c
            print(s)
        else:
            s=a-b
            print(s)
a=maths()
a.sum(5,7)

#polymor overriding
class college:
    def branch(self,ct,ee,me,ce):
        print(ct," and ",me)
class school:
     def branch(self,ct,ee,me,ce):
        print(ce," and ",ee)
school().branch(5,6,7,5)
college().branch(5,8,3,3)

