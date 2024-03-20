#partition():splits the string at the first occurrence of the separator and returns a tuple
s="python is very and it is oop and it is interpreted language"
print(s.split(" "))
print(s.partition(" "))

#startwith and endwith
s="Bhanu Teja"
print(s.startswith('a'))
print(s.startswith('bh'))
print(s.startswith('B'))
print(s.endswith('a'))
print(s.endswith(' '))

# isdigit()
s="12345"
print(s.isdigit())
s="abcABC"
print(s.isalpha())
s="1234#sai"
print(s.isalnum())

#list
l=[10,20,30,40,20.5,"Bhanu",True,None] #if i remove brackets it will truple by diffault
print(l)
print(type(l))
#index
print(l[6])
print(l[-3])
# print(l[78])#list index is out of range

#nested list
#  0  1       2                     3
#          0  1  2    3    4      5
#                  0   1    2
l=[10,20.5,[30,40.9,[10,20,"Bhanu"],True],None]
print(l[2])
print(l[2][3])
print(l[-2][-3])
print(l[2][2][2])
print(l[-2][-2][-1])

#slicing
#slicing never impact on reverse direction
l=[10,"sai",45.6,True,None,34]
print(l[::])
print(l[0:6:1])
print(l[1:5])
print(l[5:1])#empty list never impact on reverse direction
print(l[::-1])

#Adding the values in list index position
l=[10,"sai",45.6,True,None,34]
print(l)
l[1]=33 #1 is index and 33 value
print(l)
# i want sai in the list but add the value in list in these case using built in fuction insert
l=[10,"sai",45.6,True,None,34]
print(l)
l.insert(1,33) #1 is index and 33 value
print(l)
l.append(44)
print(l)
l.extend([56,"Bhanu",45.6])
print(l)