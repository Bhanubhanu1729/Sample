s="python is very easy and it is oop and it is interpreted prg language" #count
print(s.count("is")) #"is" is a sub string
print(s.count(" "))
print(s.count("a"))
print(s.count("x"))

s="python is very easy and it is oop and it is interpreted prg language"#replace
print(s)
s1=s.replace("a","A") #take new string
print(s1)
print(s.replace(" ","@")) #or direct write in print stastment

s="hyderabad" #upper and lower case
print(s)
print(s.upper())
print(s.lower())

s="DurGaSoFt"#swapcase it means lower to upper and upper to lower
print(s)
print(s.swapcase())

s="mohan" #is
print(s.islower())

s="SAI"
print(s.islower())
print(s.isupper())

print(" ".join("Mohan")) #join with reverse

l=["sai","raj","Kumar"]
print(" ".join(l))
print(" ".join(reversed(l)))

s="python is very easy" #sort
print(s)
#print(s.sort())#'str' object has no attribute 'sort'
s1=s.split(" ") #assending order
s1.sort()
print(s1)
s1.sort(reverse=True)#dessending order
print(s1)
#i want convert the list to string we can use join
print(" ".join(s1))

#excise
s="HyDeraBad Is thE Best CIty" #count the no of lower case charcater and upper characters
c=0
for i in s:
    if(i.islower()):
        c +=1
print(c)
D=0
for i in s:
    if(i.isupper()):
        D +=1
print(D)

s="HyDeraBad Is thE Best CIty" # lower case and upper case character separtely
for i in s:
    if i in s.upper():
        print(i,end="")
print()
for i in s:
    if i in s.lower():
        print(i,end=" ")

s="hyderabad"



