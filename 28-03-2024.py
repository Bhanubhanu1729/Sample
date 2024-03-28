# #MAP
# def dbl(n):
#     return 2*n
# l=[1,2,3,4,5,6,7,8,9,10]
# l1= list(map(dbl,l))
# print(l1)
#
# #with lambda
# l=[1,2,3,4,5,6,7,8,9,10]
# l1=list(map(lambda n:2*n,l))
# print(l1)

#reduce() is used to reduce the sequence of value and it will return a single value
from functools import reduce
def f1(x,y):
    return x*y

l=[1,2,3,4,5,6,7,8,9,10]
r=reduce(f1,l)
print(r)
#with lambda
l=[1,2,3,4,5,6,7,8,9,10]
r=reduce(lambda x,y:x+y,l)
print(r)

# #1.function aliasing
# def f1():
#     print("Hello Bhanu")
#
# f2=f1
# print(id(f1))
# print(id(f2))
# del f1
# f2()
#
# #nested function
# def f3():
#     print("Hello")
#
#     def f4():
#         print("Good")
#
#         def f5():
#             print("Welcome")
#
#         f5()
#     f4()
#
# f3()
# #recursive function : A function that calls itself every time is called recusive function
# #factorial(n) = n*factorial(n-1)
# def factorial(n):
#     if n == 0:
#         result =1
#     else:
#         result = n*factorial(n-1)
#     return result
# print("factorial of 3 is:",factorial(3))
#
# #anthor method
# import math
# print(math.factorial(4))
# print(math.sqrt(16))
# print(math.floor(32.6))
# print(math.pow(4,2))
#
# #only once we can write math
# from  math import  *
# print(factorial(4))
# print(sqrt(16))
# print(floor(32.6))
# print(pow(4,2))
# help(math)
#
