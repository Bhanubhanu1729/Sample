import Test32 #in this case no problem
import Test33

print(Test32.a)
print(Test33.a)
#in this case we have a problem
from Test32 import *
from Test33 import*
print(a)
print(a)
#to over come this problem
from Test32 import *
print(a)
from Test33 import*
print(a)





