#Tuple creation
t=(10,20,"sai",10.78,20,True,None)
print(t)
print(type(t))
del t
# print(t)
#slicing
t=(10,20,"sai",10.78,20,True,None)
print(t[4])
print(t[-3])
print(t[::-2])
print(t[1:3])

#count and index
t=(10,20,10,20,10,20,10,20)
print(t.count(10))
print(t.count(20))
print(t.index(20))
#memebership
print(100 in t)
print(10 in t)
print(100 not in t)
print(10 not in t)

#len , min,max and summ only number
t=(10,20,-10,20.7,10,20,12.3,20)
print(len(t))
print(max(t))
print(min(t))
print(sum(t))
t=(10,20,-10,20.7,10,20,12.3,20,"sai")
print(len(t))
# print(max(t))print(max(t))
#           ^^^^^^
# TypeError: '>' not supported between instances of 'str' and 'float'

# print(min(t))
# print(sum(t))

#convertion of string to tuple
t="Bhanu teja"
print(t)
print(type(t))
p=tuple(t)
print(p)
print(type(p))
#convertion of list to tuple
t=[10,20,30]
print(t)
print(type(t))
p=tuple(t)
print(p)
print(type(p))
#convertion of tuple to string
t=('a','b','c')
print(t)
print(type(t))
s=str(t)
print(s) #both theinput and  output are same and structure('a','b','c') but we want abc
print(type(s))
r=" ".join(t) #using join operator we geet the string
print(r)

#packing
a=10
b=20
c=30
t=a,b,c
print(t)
#unpacking
t=(13,24,56)
a,b,c=t
print("a=",a)
print("b=",b)
print("c=",c)
