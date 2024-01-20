#Abstraction
import abc
from abc import ABC,abstractmethod
class polygon(ABC):
    def side(self):
        print("abstracted method")
class tri(polygon):
    def side(self):
        print("triangle method")
class rec(polygon):
    def side(self):
        print("rectangle method")
        
class hex(rec):
    def side(self):
        super().side()        
p=hex()
p.side()

#encapsulation
class base:
    def __init__(self):
        self._a=2
        print(self._a)
      
class derived(base):
    def __init__(self):
        print()

d=derived()

import mysql.connector

db=mysql.connector.connect(host="localhost",user="root",password="",database="dom")
mc=db.cursor()
sql="update john set name='jack' where name='dominic'"
mc.execute(sql)
db.commit()

print(mc.rowcount, "record inserted.")

