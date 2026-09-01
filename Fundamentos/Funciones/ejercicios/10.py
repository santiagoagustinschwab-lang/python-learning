#10
producto_1 = {
    "Precio":100,
}
producto_2 = {
    "Precio":200,
}
producto_3 = {
    "Precio":300,
}

productos = [producto_1, producto_2, producto_3]

def producto_mas_caro (productos):
    mayor = productos[0]
    for producto in productos:
        if producto["Precio"] > mayor["Precio"]:
            mayor = producto
    return mayor


print(producto_mas_caro(productos))