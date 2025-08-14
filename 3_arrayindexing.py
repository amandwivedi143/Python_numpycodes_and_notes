# array indexing is the same as same as array start with 0 and then 1
import numpy as np
#for 1 d array
x=np.array([1,2,3,4,5])
print(x[0]) # prints 1
# for 2d array
y=np.array([
    [1,2,34,5],[2,6,8,9]
     ])
print(y[1,3])
# for 3d array note 2 2d array make a 3d array in numpy
z= np.array([
    [[2,3,4],[5,6,7]],
    [[1,2,3] ,[1,2,34]]
    ])
print(z.ndim)
print(z[1,1,2])