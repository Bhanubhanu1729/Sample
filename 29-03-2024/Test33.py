import Test32
print(Test32.a)
Test32.add(32,18)
Test32.sub(5,18)
#Module alising
import Test32 as K
print(K.a)
K.add(32,18)
K.sub(5,18)
#some time dont wont use module name or alising name in these case we ise from
from Test32 import* #* means load all the function in the this
print(a)
add(32,23)
sub(24,12)
#i use only one value in this case use name
from Test32 import a,add,sub
print(a)
add(77,23)
sub(24,12)
#Member aliasing
from Test32 import a as b,add as sum,sub
print(b)
sum(77,23)
sub(24,12)
#module information
import Test32
help(Test32)
#multiple function
a=200
def mul(x,y):
    print("mul is:",x*y)