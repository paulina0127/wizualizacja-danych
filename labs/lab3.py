import random
"""
Zad1

A = [1-x for x in range(1,11,1)]
print("A:", A)

B = [4**x for x in range(8)]
print("B:", B)

C = [x for x in B if x % 2 == 0]
print("C:", C)
"""

"""
Zad2

lista1 = []

for x in range(10):
    lista1.append(random.randrange(1,100))

a = [x for x in lista1 if x % 2 == 0]
print("Lista1:", lista1)
print("Liczby parzyste w lista1:", a)
"""

"""
Zad3

produkty = {"mleko":"litr", "ziemniaki":"kg", "masło":"gram", "chleb":"sztuka", "ser":"gram", "sok":"litr", "jajka":"sztuka"}
jednostki = {value:key for key, value in produkty.items()}

print(produkty)
print(jednostki)
"""

"""
Zad4

def trojkat(a,b,c):
    if (a**2 + b**2 == c**2):
        print("Trójkąt jest prostokątny.")
    else:
        print("Trójkąt nie jest prostokątny.")

trojkat(3,4,5)
"""

"""
Zad5

def trapez(a=0, b=0, h=0):
    return 0.5*(a+b)*h

print(trapez())
print(trapez(9,3,12))
"""

"""
Zad6

def ciag(a=1, b=4, ile=10):
    iloczyn = a
    for i in range(ile):
            iloczyn *= b
    return iloczyn

print(ciag())
print(ciag(5,2,3))
"""

"""
Zad7

def ciag(* liczby):
    if len(liczby) == 0:
        return 0
    else:
        iloczyn = 1
        for i in liczby:
            iloczyn *= i
        return iloczyn

print(ciag())
print(ciag(3,2,3,4))
"""

"""
Zad8

def zakupy(** produkty):
    suma = 0
    liczba = 0
    for i in produkty:
        liczba += 1
        suma += produkty[i]
    print("Liczba produktów: " + str(liczba) + "\n" + "Suma: " + str(suma))

zakupy(maslo=2.50, chleb=2, mleko=1.99, ser=3.59)
"""
