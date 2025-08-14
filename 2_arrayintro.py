import numpy as np
x =np.array([1,2,3,4])
y = np.array((5,6,7,8))
print(x)
print(type(x))
print(y)
print(type(y))
# for the dimenssion of array use ndim
print(x.ndim)
print(y.ndim)
# for changing the dimmison of any array use ndmin
z = np.array([1,2,3,4,5] , ndmin=5)
print(z)
print(z.ndim)
