from array import *
import numpy as np
a = array("i",[])
b = array("i", [])
n = int(input("Enter Length : "))


for i in range(n):
    x=int(input("Enter first array values : "))
    a.append(x)

for i in range(n):
    y=int(input("Enter the second array values : "))
    b.append(y)
eq = np.allclose(a, b)
m = np.array(a)
n = np.array(b)
print(m)
print(n)
print(eq)
