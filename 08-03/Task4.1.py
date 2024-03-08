s="hyderabad"  #slicing
print("Even index position characters:",s[0::2])
print("Odd index position characters:",s[1::2])

s="hyderabad"  #by using for loop
for i in range(len(s)):
    if i%2==0:
        print(s[i],end=" ")
print()
for i in range(len(s)):
    if i%2!=0:
        print(s[i],end=" ")
print()

s="hyderabad"  #by using while loop
i=0
while i < len(s):
    if i%2==0:
        print(s[i],end=" ")
        i += 2
print()
i=1
while i < len(s):
        print(s[i],end=" ")
        i += 2