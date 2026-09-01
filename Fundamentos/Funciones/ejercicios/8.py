def filtrar_pares (*numeros):
    lista_de_pares = []
    for i in numeros:
        if i % 2 == 0:
            lista_de_pares.append(i)
        else:
            continue
    return lista_de_pares

print(filtrar_pares(1,2,3,4))