#Method
class Employee:
    id=20;
    name="Dom"
    def display(self):
        print("Name:%s Age:%d"%(self.name,self.id))
d=Employee()
d.display()


#Constractor
class Joy:
    def __init__(self,name,id):  
        self.id=id;
        self.name=name;
    def display(self):
        print("Name:%s Age:%d"%(self.name,self.id))
emp1=Joy("dom",20)
emp2=Joy("chris",17)
emp1.display();
emp2.display();


#Count using constractor
class pop:
    count=0
    def __init__(self):
        pop.count=pop.count+1
s1=pop()
s2=pop()
s3=pop()
print(pop.count)


#Non para constractor
class boys:
    def __init__(self):
        print("")
    def show(self,name):
        print(name)
b=boys()
b.show("john")


#Para Constractor
class stud:
    def __init__(self,name):
        self.name=name
    def show(self):
        print(self.name)
s=stud("dom")
s.show()


#Getter and Setter
class Getset:
    def __init__(self,name,id,age):
        self.name=name;
        self.id=id;
        self.age=age;
        
s=Getset("dom",1,20)
setattr(s,"age",21)


