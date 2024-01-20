#Loop
a=int(input("enter limit:"))
s=0
for i in range(1,a+1):
    s=s+i
print("sum :",s)

j=1
f=1
while(j<=a):
    f=f*j
    j=j+1
print("factorial :",f)
