#7
def mayor_de_la_lista (*numeros):
    mayor = numeros[0]
    for i in numeros:
        if i > mayor:
            mayor = i
    return mayor


print(mayor_de_la_lista(1, 2, 3))