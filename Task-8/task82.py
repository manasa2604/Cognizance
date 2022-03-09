from array import *
import numpy as np
a = array("i",[])
b = array("i", [])
n = int(input("enter length : "))


for i in range(n):
    x=int(input("enter the first array values"))
    a.append(x)

for i in range(n):
    x=int(input("enter the second array values"))
    b.append(x)
eq = np.allclose(a, b)
print(a)
print(b)
print(eq)
