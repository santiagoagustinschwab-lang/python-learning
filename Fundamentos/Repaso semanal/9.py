#9
tupla = ("santiago", "schwab", 17, 1.70, "monte grande")

lista = list(tupla)
del lista[2]
tupla = tuple(lista)
print(type(tupla), tupla)
