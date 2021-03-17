def n_ty_wyraz(a_1, n, q):
    wyraz = a_1 * (q ** (n-1))
    return wyraz


def suma(a_1, n, q):
    if q == 1:
        suma = a_1 * n
    else:
        suma = a_1 * ((1 - q ** n) / (1 - q))
    return suma


def srodkowy_wyraz(x, z):
    y = x * z
    for i in range(y):
        if i * i == y:
            y = i
    return y
