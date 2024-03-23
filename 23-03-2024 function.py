#single function in single task is best in reality not a multiple task
#multiple task
def f1(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    return sum,sub,mul
x,y,z=f1(20,10)
print("sum is:",x)
print("sub is:",y)
print("mul is:",z)

#single function in single task
# def sum(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# print("sum is:",sum(10,20))
# print("sub is:",sub(20,10))
#write a program to perform the arithmetic operation like add,sub,mul,div by accepting two numbers from the user and also by accepting the choice from the user
def sum(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return(a/b)
choice= int(input("Enter your choice:"))
if choice >0 and choice <=4:
    a=int(input("Enter the first number:"))
    b=int(input("Enter the second number:"))
    if choice ==1:
        print("sum is:",sum(a,b))
    elif choice == 2:
        print("sub is:",sub(a,b))
    elif choice == 3:
        print("mul is:",mul(a,b))
    elif choice == 4:
        print("div is:",div(a,b))
else:
    print("Invalid choice:")





