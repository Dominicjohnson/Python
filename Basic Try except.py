#Try and except
def dom(n):
    print('Means:'+n)
love={"nature":"water","Mind":"peace",'country':'finland'}

try:
    a=int(input("enter value:"))
    b=int(input("enter value:"))
    c=a/b
    print("division:%d"%c)
except ZeroDivisionError:
    print("invalid value by zero")
except Exception:
    print('Error occurred')
else:
    print('no Error')
username = input('Enter name:')
print("username is:"+username)
