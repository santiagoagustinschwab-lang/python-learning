def dividir_seguro(a, b):
    division = a / b
    if b == 0:
        print("no se puede dividir por 0")
    else:
        return division

print(dividir_seguro(10, 0))