import numpy as np
"""
Zad1

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a*b)
"""

"""
Zad2

a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
b = np.array([[5, 4, 5, 1], [9, 8, 5, 3], [3, 6, 6, 5], [9, 0, 3, 1]])

for i in range(3):
    minW = a[i][0]
    minK = a[0][i]
    for j in range(3):
        if a[i][j] < minW:
            minW = a[i][j]
        if a[j][i] < minK:
            minK = a[j][i]
    print("Wiersz " + str(i+1) + ": " +  str(minW))
    print("Kolumna " + str(i+1) + ": " + str(minK) + "\n")

for i in range(4):
    minW = b[i][0]
    minK = b[0][i]
    for j in range(4):
        if b[i][j] < minW:
            minW = b[i][j]
        if b[j][i] < minK:
            minK = b[j][i]
    print("Wiersz " + str(i+1) + ": " +  str(minW))
    print("Kolumna " + str(i+1) + ": " + str(minK) + "\n")
"""

"""
Zad3

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a.dot(b))
"""

"""
Zad4

a = np.array([-1, -2, 3])
b = np.array([4.5, 5, 6.2])

print(a * b)
"""

"""
Zad5

m = np.array([[1.5, 2],[4, 5.2], [9, 3]])
a = np.sin(m)

print(a)
"""

"""
Zad6

m = np.array([[5, 10],[1.4, 9.1], [6, 44]])
b = np.cos(m)

print(b)
"""

"""
Zad7

def dodaj(a,b):
    c = a + b
    return c

print(dodaj(a,b))
"""

"""
Zad8

a = np.arange(1,10,1)
a = a.reshape(3,3)

for i in a:
    print(i)
"""

"""
Zad9

a = np.arange(1,10,1)
a = a.reshape(3,3)

for i in a.flat:
    print(i, end=" ")
"""

"""
Zad10

a = np.arange(1,82,1)

a = a.reshape(9,9)
print(a)
a = a.reshape(27,3)
print(a)
"""

"""
Zad11
"""