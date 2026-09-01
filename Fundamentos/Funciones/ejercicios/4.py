suma = 0

def sumar_todos(*numeros):
    suma = 0
    for i in numeros:
        suma = suma + i
    return suma

print(sumar_todos(1, 2, 3, 4))

