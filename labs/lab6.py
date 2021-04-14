import numpy as np
"""
Zad1

tab = np.arange(4, 81, 4)

print(tab)
"""

"""
Zad2

tab = np.arange(5, dtype='float')
print(tab.dtype)

tab1 = tab.astype('int32')
print(tab1)
print(tab1.dtype)
"""

"""
Zad3

def tablica(n):
    tab = np.empty((n, n))
    tab = tab.astype('int')
    s = 0
    for i in range(n):
        for j in range(n):
            tab[i, j] = (2**s)
            s += 1
    print(tab)

print(tablica(4))
"""

"""
Zad4

def generuj(a, b):
    tab = np.logspace(1, b, num=b,base=a, dtype=int)
    print(tab)

generuj(2,4)
"""

"""
Zad5

def diagonalna(n):
    diag = np.diag([a for a in range(n,0,-1)], +2)
    print(diag)

diagonalna(3)
"""

"""
Zad6

tab = np.array([['L','A','K','O','T','F'],['T','O','M','Z','L','B'],['M','L','W','A','P','O'],['K','W','I','A','T','G'],['H','K','D','Y','B','A']])

print(tab)
"""

"""
Zad7
"""

"""
Zad8
"""

"""
Zad9

tab = np.arange(0, 100, 4)
tab = tab.reshape(5, 5)

print(tab)
"""