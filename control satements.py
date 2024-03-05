# i=int(input("enter first number:"))
# j=int(input("enter second number:"))
# if i > j:
#     print(i,"is big")
# else:
#     print(j,"is big")

i=int(input("enter first number:"))  #Nested if
j=int(input("enter second number:"))
k=int(input("enter thrid number:"))
if i > j and  i > k:
    print(i,"is big")
else:
    if j>k:
     print(j,"is big")
    else:
       print(k,"is big")
