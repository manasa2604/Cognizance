from array import*
import numpy as np
array = array("i",[])
a = int(input("Enter the Length : "))
for i in range(a):
    x = int(input("Enter Values : "))
    array.append(x)

A = np.array(array)
new = A.astype("float")
print(array)
print(new)
print(new.dtype)

