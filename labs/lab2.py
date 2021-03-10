import sys as system
"""
Zad1

lista = ['Zmierzch','Iron Man','Biały wąż','WALL-E','Love, Rosie','Titanic','Avengers','Wolverine']
lista.reverse()
print(lista)

lista.insert(5,'Król Lew')
lista.insert(5,'Zaplątani')
print(lista)
"""

"""
Zad2

filmy = {"A1":"Avengers", "B1":"Biały wąż", "I1":"Iron Man", "K1":"Król Lew", "L1":"Love, Rosie", "T1":"Titanic", "W1":"WALL-E", "W2":"Wolverine", "Z1":"Zaplatani", "Z2":"Zmierzch"}
"""

"""
Zad3

przedmioty = {"CAD":"CAD komputerowe wspomaganie programowania", "PS":"Programowanie struktualne", "KKP-WiJK":"Kultura kresów północno-wschodnich i jej kontynuacja", "JA":"Język angielski", "AMDI":"Analiza matematyczna dla informatyków", "WD":"Wizualizacja danych", "MDDI":"Matematyka dyskretna dla informatyków"}

print(u"Liczba elementów to:", len(przedmioty))
"""

"""
Zad4

liczba = input("Podaj liczbę typu float.")
liczba = float(liczba)
pot = liczba ** liczba
print("Wynik:", pot)
"""

"""
Zad5

system.stdout.write("Podaj napis.")
napis = system.stdin.readline()
print(u"Wystąpienia litery 'a':", napis.count("a"))
"""

"""
Zad6

a = input(u"Podaj pierwszą liczbę.")
b = input(u"Podaj drugą liczbę.")
c = input(u"Podaj trzecią liczbę.")
a = int(a)
b = int(b)
c = int(c)

if (a % 2 == 0) & (b > c):
    print("Tak")
else:
    print("Nie")
"""

"""
Zad7

lista = [1, 3.5, 4, 5, 9.1, 2]
suma = 0
r = len(lista)

for x in range(1, r):
    suma = lista[x] + lista[x-1]
    print(suma)
"""

"""
Zad8

i = 1
parzyste = []

while (i <= 10):
    i +=  1
    liczba = input("Podaj liczbę.")
    liczba = int(liczba)
    if liczba % 2 == 0:
        parzyste.append(liczba)

print(parzyste)
"""

"""
Zad9

lista = [1,2,3,4,5,6]

for x in lista:
    if (x == 1) | (x == 6):
        print("O" * 6)
    else:
        print("O" + " " * 4 + "O")
"""

"""
Zad10

liczba = input("Podaj liczbę.")

try:
    liczba = int(liczba)
except ValueError:
    print("Błąd. Wprowadzone dane nie są liczbą.")
"""