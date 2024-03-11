s="python is very easy" #reverse each word of the string
print(s)
s1=s.split(" ")
for i in s1:
    print(i[: :-1],end=" ")
print()

s="durgasoft" #display vowels in a given string
for i in s:
    if i in 'aeiou':
        print(i,end=" ")