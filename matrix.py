from numpy import *
arr1 = array([

               [1, 2, 3, 9],
               [4, 5, 6, 2]

            ])
m = matrix(arr1)
print(m)


m1 = matrix('1 2 3; 6 4 5; 6 7 8')
m2 = matrix('1 2 3; 6 4 5; 6 7 8')
m3 = m1 * m2
m3 = m1 + m2

print(m3)

print(diagonal(m))
print(m.min())
print(m.max())