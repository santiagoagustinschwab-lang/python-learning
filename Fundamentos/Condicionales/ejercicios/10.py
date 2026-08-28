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

lista = [producto_1, producto_2, producto_3]

if lista[0]["Precio"] < lista[1]["Precio"] and lista[0]["Precio"] < lista[2]["Precio"]:
    print("El primer producto es el mas barato")
elif lista[0]["Precio"] > lista[1]["Precio"] and lista[2]["Precio"] > lista[1]["Precio"]:
    print("el segundo es el mas barato")
else:
    print("El tercer producto es el mas barato")