l=[10,20,30,40]
print(l)
print(type(l))
b=bytes(l)
print(b)
print(type(b))
for i in b:
    print(i,end=" ")
#bytearray
l=[10,20,30,40]
print(l)
print(type(l))
b=bytearray(l)
print(b)
print(type(b))
b[1]=66
for i in b:
    print(i,end=" ")
#frozen set
s={10,20,30,40}
print(s)
print(type(s))
fs=frozenset(s)
print(fs)
print(type(fs))


#FUNCTION
def f1():
    for i in range(5):
        print("Bhanu",end=" ")
f1()
print()
#passing parameters
def my_fun(name):
    print("Hello:",name)
my_fun("Bhanu")
my_fun("RCB")
#2
def square(n):
    print("The square of",n,"is:",n*n)
square(32)
square(n=int(input("Enter a number:")))

3
def even_odd(n):
     if n%2==0:
         print("Number is even:",n)
     else:
         print("Number is odd :",n)
even_odd(n=int(input("enter a number")))

#4
def f1(n):
    if n in range(1,101):
        print("is in range of 1 to 100:",n)
    else:
        print("is in out of range:",n)
f1(n=int(input("enter a number:")))

