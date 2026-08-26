#1
producto = {
    "Nombre":"Taza",
    "Precio":200,
    "Stock":10,
    "Categoria":"Dia a dia",
}

print(producto["Precio"])

#2
print(producto["Stock"] - 1)

#3
producto["Marca"] = "Generica"
print(producto)

#4
del producto["Categoria"]
print(producto)

#5
print("Precio" in producto)
print("Envio" in producto)

#6
print(producto.items())

#7
print(producto.keys())
print(producto.values())

#8
lista = list(producto.keys())
print(len(lista))

#9, lo que pasa es que la pupla utiliza parentecis en vez de llaves pero la principal diferencia es que el set esta desordenado
tupla = tuple(producto)
set = set(producto)

print(tupla)
print(set)

#10
persona = {
    "Nombre":"Martin",
    "Edad":20,
}
print(producto, persona)