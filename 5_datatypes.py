# i for int
# b for boolean
# u for unsigned integer
# f for float
# S for the string 
# c for complex float 
# m for timedata
# O for object
# M for datetime 
# V for memory
# U unicode string
import numpy as np
x= np.array([1,2,3,4,5])
print(x.dtype)
y= np.array(['apple','banana','cherry'])
print(y.dtype)
# using define datatype
z= np.array([1,2,3,4,5] ,dtype='S')
print(z.dtype)
print(z)
# converstion or casting 
a = np.array([1,2,3,4,5])
b=a.astype('f')
print(b.dtype)
print(b)