from numpy import *

arr1 = array([

               [1, 2, 3, 9, 8, 7],
               [4, 5, 6, 2, 9, 1]



            ])

arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,3)

print(arr1.dtype)
print(arr1.ndim)
print(arr1.shape)
print(arr1.size)

print(arr2)
print(arr3)