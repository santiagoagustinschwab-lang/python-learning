

def recibir_lista(lista, indice):
    numero = lista[indice]
    print(numero)



numeros = [10, 20, 30]

try:
    recibir_lista(numeros, 2)
except IndexError:
    print("el indice no existe en la lista")