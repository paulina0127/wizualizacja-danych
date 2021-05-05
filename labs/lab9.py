import pandas as pd
import matplotlib.pyplot as plt

"""
Zad1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)

grupa = df.groupby(['Rok']).agg({'Liczba':['sum']})
grupa.plot()
plt.show()
"""

"""
Zad2

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})

wykres = grupa.plot.bar()
wykres.set_ylabel("Mln")
wykres.set_xlabel("Płeć")
wykres.legend()
plt.title("Liczba urodzonych dzieci z podziałem na płeć")
plt.xticks(rotation=0)
plt.show()
"""

"""
Zad3

licz = df[df['Rok'] >= 2012]
grupa = licz.groupby(['Plec']).agg({'Liczba':['sum']})

wykres = grupa.plot.pie(subplots=True,autopct
='%.2f %%',fontsize=20, figsize=(6,6), legend=(0,0))
plt.legend(loc="lower right")
plt.title("Ilość urodzonych chłopców i dziewczynek w latach 2012-2017")
plt.show()
"""

"""
Zad4

df = pd.read_csv('zamowienia.csv', header=0, index_col=0, sep=";", decimal='.', parse_dates=True)

grupa = df.groupby(['Sprzedawca']).size().reset_index(name="Zamowienia")
wykres = grupa.plot.bar()
wykres.set_ylabel("Zamówienia")
wykres.set_xlabel("Sprzedawcy")
wykres.legend()
plt.title("Liczba zamówień poszczególych sprzedawców")
plt.xticks(rotation=0)
plt.show()
"""


