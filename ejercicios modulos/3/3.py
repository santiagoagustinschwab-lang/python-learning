

try:
    numero_1 = int(input("Ingrese el primer numero: "))
    numero_2 = int(input("Ingrese el segundo numero: "))
    print(numero_1 + numero_2)
except ValueError:
    print("ingresa un numero, no una palabra")
