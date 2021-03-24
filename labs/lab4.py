import sys
import random

"""
Zad1

lista = []

for x in range(10):
    lista.append(random.randrange(30)*2)

plik = open("liczby.txt","w+")
plik.writelines(str(lista))
plik.close()
"""

"""
Zad2

plik = open("liczby.txt","r")
wiersze = plik.readlines()
plik.close()

print(wiersze)
"""

"""
Zad3

with open("tekst.txt", "w+") as plik:
    for i in range(3):
        linia = sys.stdin.readline()
        plik.write(linia)

with open("tekst.txt", "r") as plik:
    for wiersz in plik:
        print(wiersz, end="")
"""

"""
Zad4

class NaZakupy:
   """Lista produktów"""
    def __init__(self, nazwa_produktu, ilosc, jednostka_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednostka_miary = jednostka_miary
        self.cena_jed = cena_jed

    def wyswietl_produkt(self):
        info = "Nazwa produktu: " + self.nazwa_produktu
        return info

    def ile_produktu(self):
        ile = "Ilość: " + self.ilosc + " " + self.jednostka_miary
        return ile

    def ile_kosztuje(self):
        koszt = "Koszt: " + str(int(self.ilosc) * int(self.cena_jed))
        return koszt

nazwa = input("Podaj nazwę produktu.")
ilosc = input("Podaj ilość produktu.")
jednostka = input("Podaj jednostkę produktu.")
cena = input("Podaj cenę produktu.")
print("\n")

zakupy = NaZakupy(nazwa,ilosc,jednostka,cena)
print(zakupy.wyswietl_produkt())
print(zakupy.ile_produktu())
print(zakupy.ile_kosztuje())
"""

"""
Zad5

class CiagArytmetyczny:
   """Obliczanie ciągów arytmetycznych"""

    def __init__(self, a_1, r, n):
        self.a_1 = a_1
        self.r= r
        self.n = n
        self.elementy = []


    def wyswietl_dane(self):
        print(self.elementy)


    def pobierz_elementy(self):
        ile = input("Podaj ilość elementów.")

        for i in range(int(ile)):
            e = input("Podaj wartość ciągu.")
            e = int(e)
            self.elementy.append(e)


    def pobierz_parametry(self):
        self.a_1 = input("Podaj pierwszy wyraz ciągu.")
        self.r = input("Podaj różnicę ciągu.")
        self.n = input("Podaj liczbę elementów ciągu.")


    def policz_sume(self):
        suma = 0
        for i in range(len(self.elementy)):
            suma += self.elementy[i]
        return suma


    def policz_elementy(self):
        a = int(self.a_1)
        x = int(self.n)

        for i in range(x):
            self.elementy.append(a)
            a += int(self.r)


ciag = CiagArytmetyczny(1,1,1)

print(ciag.pobierz_elementy())
print(ciag.wyswietl_dane())
print(ciag.pobierz_parametry())
print(ciag.policz_elementy())
print(ciag.policz_sume())
"""