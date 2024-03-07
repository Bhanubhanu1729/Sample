n=int(input("Enter the number:")) #by using while print sum of first number
i=1
s=0
while i<=n:
    s=s+i
    i=i+1
print("The sum of first",n,"Number is:",s)


n=int(input("Enter the number:")) #by using for loop print sum of first number
s=0
for i in range(1,n+1):
    s=s+i
print("sum of first",n,"number is:",s)