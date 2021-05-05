import pandas as pd
import xlrd
import openpyxl

"""
Zad1

xlsx = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(xlsx, header=0)
print(df)
"""

"""
Zad2

#1
print(df[df['Liczba']<1000])
#2
print(df[df['Imie']=='PAULINA'])
#3
print(df['Liczba'].sum())
#4
print(df[(df['Rok'] >= 2005) & (df['Rok'] <= 2010)]['Liczba'].sum())
#5
print(df[(df['Rok'] == 2000) & (df['Plec'] == 'M')]['Liczba'].sum())
#6
print(df.loc[df.groupby(['Rok','Plec'])['Liczba'].idxmax()])
#7
w = df.groupby(['Plec','Imie'])['Liczba'].sum().reset_index(name="Suma").sort_values(by="Suma",ascending=False)
print(w[0:2])
"""

"""
Zad3

df = pd.read_csv('zamowienia.csv', header=0, sep=";",decimal='.',parse_dates=True)
print(df)
#1
print(df['Sprzedawca'].drop_duplicates())
#2
print(df.sort_values(by='Utarg', ascending=False)['Utarg'][0:5])
#3
print(df.groupby(['Sprzedawca']).size().reset_index(name='Zamowienia'))
#4
print(df.groupby(['Kraj']).size().reset_index(name='Zamowienia'))
#5
df['Data zamowienia'] = pd.to_datetime(df['Data zamowienia'])
lista = df[(df['Data zamowienia'].dt.year == 2005) & (df['Kraj']=='Polska')]
print(len(lista))
#6
lista1 = df[df['Data zamowienia'].dt.year == 2004]
print(lista1['Utarg'].sum() / len(lista1))
#7
df[df['Data zamowienia'].dt.year == 2004].to_csv(index = False, header=True, sep=';', path_or_buf="E:/uni/wizualizacja/pycharm/labs/zamowienia_2004.csv")
df[df['Data zamowienia'].dt.year == 2005].to_csv(index = False, header=True, sep=';',path_or_buf="E:/uni/wizualizacja/pycharm/labs/zamowienia_2005.csv")
"""
