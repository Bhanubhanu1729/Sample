#varible length arruguments
def add(*args):
    print(sum(args))
add(10,20)
add(10,20,30)
add(2,3,4,5,6,7,8)
add(3.4,56.9,-9,23,45,67,89)
add(34,56,67,88)

def add(*args):
    s=0
    for i in args:
        s=s+i
    print(s)
add(10,20)
add(10,20,30)
add(2,3,4,5,6,7,8)
add(3.4,56.9,-9,23,45,67,89)
add(34,56,67,88)
#**kwargs:
def f1(**kwargs):
    print(kwargs)
    for k,v in kwargs.items():
        print(k,"=",v)
f1(a=10,b=20,c=18)
f1(id=18,name="Kohli",address="RCB",age="35")
#positional only arguments
def add(a,b):#with out positional only arguments
    print("sum is:",a+b)
add(10,20)
add(a=10,b=20)

def add(a,b,/):#positional only arguments using /(forword salcing)
    print("sum is:",a+b)
add(10,20)
#add(a=10,b=20)TypeError: add() got some positional-only arguments passed as keyword arguments: 'a, b'
#keyword only arguments:
def add(*,a,b):#positional only arguments using *(forword salcing)
    print("sum is:",a+b)
#add(10,20)TypeError: add() takes 0 positional arguments but 2 were given
add(a=10,b=20)

s=lambda n:n*n
print(s(6))
s=lambda a,b:a+b
print(s(3,4))
s=lambda a,b:a if a>b else b
print(s(6,3))
s=lambda a,b,c: a if a>b and a>c else b if b>c else c
print(s(5,9,3))
s=lambda n:"is even" if n%2==0 else "is odd"
print(s(5))
print(s(8))