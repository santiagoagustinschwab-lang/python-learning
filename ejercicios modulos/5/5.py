try:
    numero = int(input("ingrese un numero"))
except:
    print("ingrese un numero no una letra")
else:
    print(numero * 2)
finally:
    print("Fin del programa")