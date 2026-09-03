try:
    numero_1 = int(input("ingrese el primer numero: "))
except ValueError:
    numero_1 = 0
    print("Ingrese un numero no una palabra")
try:
    numero_2 = int(input("ingrese el segundo numero: "))
except:
    numero_2 = 0
    print("ingrese un numero no una palabra")
try:
    numero_3 = int(input("ingrese el tercer numero: "))
except:
    numero_3 = 0
    print("ingrese un numero una palabra")
finally:
    suma = numero_1 + numero_2 + numero_3
    print(suma)