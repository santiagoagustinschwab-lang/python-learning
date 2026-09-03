from validacion import es_mayor_de_edad

try:
    edad = int(input("Ingrese tu edad: "))
except ValueError:
    print("ingrese un numero no una palabra")
else:
    print(es_mayor_de_edad(edad))