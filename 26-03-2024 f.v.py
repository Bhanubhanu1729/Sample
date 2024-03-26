#local varible
def f1():
    a=100
    print(a)

def f2():
    b=200
    print(b)

f1()
f2()
#Global varibles:
a=100
def f1():
    a=99#local varible id first priority
    print(a)
def f2():
    print(a)

f1()
f2()

#global keyword
a=100
def f1():
    global a
    a=99
    print(a)
def f2():
    print(a)

# f1() #output:99
# f2()#output:99
f2()#output:100
f1()#output:99

#if local and golobal name are same how to accsess both
a=100
def f1():
    a=99
    print(a)
    print(globals()['a'])
def f2():
    print(a)

f1() #output:99
#output:100
f2()#output:99

#positional arguments
def sub(a,b):
    print("sub is:",a-b)

sub(10,20)
sub(20,10)
# sub(10)TypeError: sub() missing 1 required positional argument: 'b'

#keyword argument
def f1(name,msg):
    print("Hello:",name,msg)
#positinal argiments
f1("Bhanu","Good night")
f1("Good night","Bhanu")
#keywords arguments
f1(name="Bhanu",msg="Good night")
f1(msg="Good night",name="Bhanu")

#we can also use one postional and one keyword args
#but make sure that first we have to mention postional args then after
f1(name="Bhanu",msg="good evening")
#default arguments
def f1(course="python"):
    print("couse name:",course)

f1("c")
f1()
f1("c++")
f1()
#non default value
def f1(name,course="python"):
    print(name,"couse name:", course)


f1("sai","c")
f1("Bhanu")
f1("Teja","java")
f1("Giri")
#varible length
def f1(n):
    print(n)
f1(10)
# f1()TypeError: f1() missing 1 required positional argument: 'n'
# f1(10,20,30)TypeError: f1() missing 1 required positional argument: 'n'
#in this cas we use *
def f1(*n):
    print(n)
f1(10)
f1(10,10,2,3,-11.2)
#sum
def f1(*n):
    print(sum(n))
f1(10)
f1(10,10,2,3,-11.2)
