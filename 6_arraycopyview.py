#copy vs view 
# copy is actuacl value while view just use for the reflection
# copy have own memory while view refelect he changes in the original array
# Example for the copy
import numpy as np
x= np.array([1,2,3,4,5])
y = x.copy()
x[0]=42
print(x)   
print(y)
#here only change will happen in the original array x
# Example for the view 
a = np.array([1,2,3,5,4])
b=a.view()
a[0]=33
print(a)
print(b) 
#here change will happen in the original array a and also in the view b