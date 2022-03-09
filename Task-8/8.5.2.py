from array import *
import numpy as np
X = array("i", [])
Y = array("i", [])
n=int(input("Enter the Length : "))
for i in range(n):
    x = int(input("Enter first array values : "))
    X.append(x)
for i in range(n):
    y = int(input("Enter second array values : "))
    Y.append(y)
m = np.array(X)
n = np.array(Y)
print(m)
print(n)
p = np.where(m == n)
print("Positions where elements of 2 numpy arrays match : ")
print(p)
