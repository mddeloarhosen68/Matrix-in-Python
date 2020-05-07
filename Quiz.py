from numpy import *

# taking inputs from user


a = int(input("enter number of rows for array A:"))
b = int(input("enter the number of columns for array a:"))

a1 = int(input("enter the number of rows for array B:"))
b1 = int(input("enter the number of columns for array B :"))

n1 = a*b
n2 = a1*b1
n3 = a*b1
A = zeros(n1, int).reshape(a, b)
B = zeros(n2, int).reshape(a1, b1)

print("enter values for Array A:")
for i in range(a):
    for j in range(b):
        val = int(input())
        A[i][j] = val


# printing Array A

print("Array A:")
for i in range(a):
    for j in range(b):
        print(A[i][j], end=" ")
    print()


print("enter the values for Array B:")
for i in range(a1):
    for j in range(b1):
        val = int(input())
        B[i][j] = val

# printing array B


print("Array B:")
for i in range(a1):
    for j in range(b1):
        print(B[i][j], end=" ")
    print()

arr = zeros(n3, int).reshape(a, b1)

# performing multiplication of 2 matrices


if b != a1:
    print("multiplication not possible")

else:

    add = 0
    for i in range(a):
        for j in range(b1):
            for k in range(b):
                add += A[i][k] * B[k][j]
            arr[i][j] = add
            add = 0


# printing final array


    print("final matrix is")
    for i in range(a):
        for j in range(b1):
            print(arr[i][j], end=" ")
        print()