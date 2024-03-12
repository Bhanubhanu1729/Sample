#excise 11-03-2024 sir write the program
s="HyDeraBad Is thE Best CIty" # 1.lower case and upper case character separtely 2nd one correct
for i in s:
    if i.islower():
        print(i,end=" ")
print()
for i in s:
    if i.isupper():
        print(i,end=" ")
print()
#3rd program write a program to convert the uppercase charcater in even index position chracter
s="hyderabad"
print(s)
for i in range(len(s)):
    if i % 2 == 0:
        s=s.replace(s[i],s[i].upper())
print(s)

#strip concept
s="    durga   "
print(s)
print(s.strip(" "))
print(s.lstrip(" "))
print(s.rstrip(" "))
print()
s="adurga"
print(s)
print(s.strip("a"))
print(s.lstrip("a"))
print(s.rstrip("a"))
 #length of string
s="Python full stack"
print(len(s))
s=" "
print(len(s))

#Find():
s="python is very easy and it is oop and it is interpreted prg language"
print(s.find("is"))
print(s.find("x"))
print(s.find(" "))

#index
s="python is very easy and it is oop and it is interpreted prg language"
print(s.index("is"))
print(s.rindex("is"))
