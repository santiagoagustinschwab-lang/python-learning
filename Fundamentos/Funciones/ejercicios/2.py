#2
def calcular_precio_final (precio, descuento = 10):
    precio_final = precio - precio * descuento / 100
    return precio_final

print(calcular_precio_final(1000))
print(calcular_precio_final(1000, 20))