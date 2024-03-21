#adda and update in set
s={10,20,30,40}
print(s)
print(type(s))
s.add(89)
print(s)
s.update([67,"bhanu",56])
print(s)
#remove elements from set (discard and remove),clear(),del
s.discard(40)
s.remove(10)
s.discard(100)
# s.remove(100) #KeyError: 100 value not in set it will show the error in discard it will not show the error
s={1020,30,40}
print(s)
s.clear()
print(s)
del s
# 3.set operation---- union(|) or a.union(b)
# #                     intersection(&)
# #                     diffrence(-)
# #                     symmetric difference(^)
a={1,2,3,4,5}
b={4,5,6,7,8}
print(a|b)
print(a.union(b))
print(a&b)
print(a.intersection(b))
print(a-b)
print(b-a)
print(a.difference(b))
print(a^b)
print(a.symmetric_difference(b))

#DICTIONARY
d={1:{10,20,30},2:"sai",3:"sai"}
print(d)
print(type(d))
#accessing values from dictionary to get accessing valuse using keys are using or get function
d={"id":123,"name":"raj","address":"hyderabad"}
print(d)
print(d["name"])
print(d.get("name"))
# print(d["age"])#key error
print(d.get("age"))
# change or add values
print(d)
d["name"]="Bhanu"
print(d)
d["age"]="21"
print(d)
#delete or remove values
del d["name"]#delete one of the key
print(d)
del d #complete delete
#copy
d={"id":123,"name":"raj","address":"hyderabad"}
print(d)
d1=d
print(d1)
d["name"]="bhanu"
print(d)
print(d1)
print(id(d))
print(id(d1))
#-Deepcopy
d={"id":123,"name":"raj","address":"hyderabad"}
print(d)
d1=d.copy
print(d1)
d["name"]="bhanu"
print(d)
print(d1)
print(id(d))
print(id(d1))
#items,keys and values
d={"id":123,"name":"raj","address":"hyderabad"}
print(d.items())
print(d.keys())
print(d.values())
#membership test only appilicable in keys not values
print(123 in d)
print(123 not in d)
print("id" in d)
print(len(d))
#pop and popitems
# pop method return the value
value=d.pop("name")
print(value)
print(d)
# pop item which is the last item that will be delete
value=d.popitem()
print(value)
print(d)
print()
value=d.popitem()
print(value)
print(d)

