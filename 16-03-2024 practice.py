# 1.strip-it return a copyof the string with both leading and trailing characters removed
s="    Bhanu    "
print(s)
print(s.strip(" "))
print(s.lstrip(" "))#lsrtip remove left side space
print(s.rstrip(""))#rstrip romove right side space

#2.len it return length of the string
s="Gopal Nagar Near Alwal"
print(s.islower())
print(len(s))

#3.Find and Index
s="python is very and it is oop and it is interpreted language"
print(s.find("is"))
print(s.index("is"))
print(s.find("teja")) #it return the-1
# print(s.index("teja"))#it return the  value error
print(s.rindex("is")) #highest sub

#4.Max and Min Depends upon the ASCII number deffrentvalues  from both the upper case and lower case
s="hyderabad"
print(max(s))
print(min(s))
# print ASCII number (American standard code for information interchages)
print(ord("y"))
print(ord("a"))

s="HYDERABAD"
print(max(s))
print(min(s))
print(ord("Y"))
print(ord("A"))
s="hyd erabad"
print(max(s))
print(min(s)) #min value is space space alse consider the min value

#5.partition(): it return the tuple format
s="python is very and it is oop and it is interpreted language"
s1=s.split("is")
print(s1) #output:['python ', ' very and it ', ' oop and it ', ' interpreted language']
print(type(s1))# o/p <class 'list'>
s2=s.partition("is")
print(s2) # o/p: ('python ', 'is', ' very and it is oop and it is interpreted language')
print(type(s2)) #o/p: <class 'tuple'>


