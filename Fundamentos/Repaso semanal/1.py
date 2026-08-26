#1
numero_1 = int(input("primero: "))
numero_2 = int(input("segundo: "))
numero_3 = int(input("tercero: "))

numeros = {numero_1, numero_2, numero_3}
promedio = sum(numeros) / len(numeros)
print("el promedio es: ", promedio)

#2
lista = ["mate", "termo", "agua", "bombilla", "pava"]
print(lista[2:4].reverse())