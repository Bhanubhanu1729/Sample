#Data Types
#Bool
a=10
b=20
c=a<b
print(c)
print(type(a))

#complex
a=10+20j
b=20+20j
c=a+b
d=a*b
print(c)
print(d)

#string
a="Python"
s='Python classes'
z=""" Bhanu """
print(a)
print(s)
print(z)

#slice operator
s=" sumoplast"
print(s[0:5])
print(s[:7])
print(s[: :])
print(s[: : -1])

#Is operator

x=42
y=42
print(x is y)
print()

x=42
y=42
z= x is y
print(z)

x=257
y=258
z= x is y
print(z)

# arthmetic operators
a=456
b=234
print("Result:",a+b)
print("Result:",a*b)
print("Result:",a-b)
print("Result:",a/b)
print("Result:",a%b)
print("Result:",a**b)
print("Result:",a//b)
s="durga"+"3"
print(s)
s="durga"*3
print(s)

a=25#Relational opertors
b=30
print(a<b)
print(a<=b)
print(a>b)
print(a >= b)
if a<b:
    print("A is a less value is:",a)
else:
    print("B is a biggest value is:", b)
