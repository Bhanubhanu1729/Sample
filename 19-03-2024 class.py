#problems sloving
l=[10,-9,45.6,30,4,9,4,10,10,-8,-8,-9,9]
print(list(set(l))) #unorder and simple logic
l1=[]
for i in l:
    if i not in l1:
        l1.append(i)
print(l1)
#2nd problem max,min and highest number
print(max(l))
print(min(l))
l.sort()
print(l[-2])
print(len(l))
#3 print the values of lessthan values in length
for i in l:
    if i < len(l):
       print(i,end=" ")


#delete or remove elements from the list by using different methodes del,remove,pop,clear
l=[10,20,30,40,50]
l.remove(10)
print(l)
l.pop(1)
print(l)
l.clear()
print(l)
del l
# print(l) NameError: name 'l' is not defined. Did you mean: 'l1'?

# list multiplication(*) and concetination(+)
L1=["sai","raj"]
L2=["raj","tarun","bhanu"]
L3=L1+L2
l4=L1*3
print(L3)
print(l4)

#sort
l=[2,-9,3,7,5,1,0,5.7]
print(l)
l.sort()
print(l)

l=["bhanu","teja","giri"]
print(l)
l.sort()
print(l)

#copy
l=[10,20,30,40]#Shallow copy
print(l)
l1=l
print(l1)
l.append(13)
print(l)
print(l1)
print(id(l))
print(id(l1))
#Deepcopy
l=[10,20,30,40]
print(l)
l1=l.copy()
print(l1)
l.append(13)
print(l)
print(l1)
print(id(l))
print(id(l1))

#count and index
l=[30,4,50,23,34,50,50]
print(l.count(50))
print(l.index(50))







