import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xlrd
import openpyxl

"""
Zad1

a = [1/x for x in range(1,21,1)]

plt.plot(a, label="f(x) = 1/x")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("Wykres funkcji f(x) dla x ∈ [1, 20]")
plt.axis([1, len(a), 0, 1])
plt.legend()
plt.show()
"""

"""
Zad2

a = [1/x for x in range(1,21,1)]

plt.plot(a, 'g', label="f(x) = 1/x", linestyle="dotted", marker=">")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("Wykres funkcji f(x) dla x ∈ [1, 20]")
plt.axis([0, len(a), 0, 1])
plt.legend()
plt.show()
"""

"""
Zad3

x = np.arange(0,30.1,0.1)
s = np.sin(x)
c = np.cos(x)

plt.plot(x, s, 'r', label="sin(x)")
plt.plot(x, c, 'b', label="cos(x)")
plt.ylabel("f(x)")
plt.xlabel("x")
plt.title("Wykres funkcji sin(x) i cos(x) dla x ∈ [0, 30]")
plt.legend()
plt.show()
"""

"""
Zad4

x = np.arange(0,30.1,0.1)
s = np.sin(x)
c = np.sin(x*(-1))-2

plt.plot(x, s, 'b', label="sin(x)")
plt.plot(x, c, 'C1', label="sin(x)")
plt.ylabel("sin(x)")
plt.xlabel("x")
plt.title("Wykres funkcji sin(x), sin(x)")
plt.legend()
plt.show()
"""

"""
Zad5

data = pd.read_csv('iris.data', header=None, delimiter=",")
c = np.random.randint(0, 150, 150)

plt.scatter(data[0], data[1], c = c, s = abs(data[0]-data[1]))
plt.xlabel("Sepal length")
plt.ylabel("Sepal width")
plt.show()
"""

"""
Zad6

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0, index_col=0)

grupa1 = df[df['Plec'] == 'K']['Liczba'].sum()
grupa2 = df[df['Plec'] == 'M']['Liczba'].sum()
etykiety = ['Dziewczynki','Chłopcy']
wartosci = [grupa1, grupa2]

plt.subplot(3,2,1)
plt.bar(etykiety, wartosci)
plt.ylabel("Mln")
plt.xlabel("Płeć")

plt.subplot(3,2,4)
grupa3 = df[df['Plec'] == 'K'].groupby(['Rok'])['Liczba'].sum()
grupa4 = df[df['Plec'] == 'M'].groupby(['Rok'])['Liczba'].sum()

plt.plot(grupa3, label="Dziewczynki")
plt.plot(grupa4, label="Chłopcy")
plt.ylabel("Ilość urodzeń")
plt.xlabel("Rok")
plt.legend()

plt.subplot(3,2,5)
grupa5 = df.groupby(['Rok'])['Liczba'].sum()

grupa5.plot.bar()
plt.ylabel("Ilość urodzeń")
plt.xlabel("Rok")
plt.show()
"""

"""
Zad7

df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal='.',parse_dates=True)
grupa = df.groupby(['Sprzedawca']).size().reset_index(name="Zamowienia")
dane = grupa['Zamowienia']
etykiety = grupa['Sprzedawca']

wedges, texts, autotexts = plt.pie(dane, labels=etykiety, autopct=lambda pct: "{:.1f}%".format(pct, textprops=dict(color="black")), shadow=True, explode = (0.1, 0, 0, 0, 0, 0, 0, 0, 0))
plt.setp(autotexts, size=14, weight="bold")
plt.title("Zamówienia poszczególnych sprzedawców")
plt.legend(title="Sprzedawcy", loc="lower left", bbox_to_anchor=(-0.4, -0.15))
plt.show()
"""
