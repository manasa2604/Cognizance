import numpy as np
a = np.array([10,11,12,13,14])
x = 6
y = np.zeros(25)
y[::x] = a
print(y)
