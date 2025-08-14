import numpy as np
# slicing in the 1d array
x= np.array([1,2,3,4])
print(x[1:3])
print(x[:3])
print(x[0:])
# slicing in 2d array
y=np.array([
    [1,2,3],
    [4,5,6],
])
print(y[0:2 ,0:1 ])
# slicing in the 3d array
z=np.array([
    [[1,2,3],[4,5,6]],
    [[7,8,9],[10,11,12]]
])
print(z[::1])
