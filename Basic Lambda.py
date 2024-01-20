#Lambda
a=lambda x:x*10
print(a(5))
b=lambda a,c:a+c
print(b(5,8))

def levelone(n):
    return lambda a:a*n
jack=levelone(5)
cat=levelone(8)
print(jack(6))
print(cat(8))

def game(l):
    return lambda d,c:(d+l)*c
target=game(1)
over=game(2)
print(target(12,6))
print(over(24,12))


bikes=['ducati','BMW','KTM','RE','jawa']
x=bikes[4]
bikes.pop(3)
bikes.remove('BMW')
bikes[2]='bajaj'
print(bikes)
l=len(bikes)
print(l)
bikes.append('BMW')
print(bikes)
new=bikes.copy()
print(new)
print(new.count('KTM'))

#File handling
import jawa
jawa.dom('learn from lords')
d=jawa.love["country"]
print(d)

