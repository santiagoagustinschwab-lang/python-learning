#5
agenda = {
    "Nombre":"Santiago",
    "Edad": 17,
    "Ciudad":"Mg",
}

nombre_busca = input("Introduce un posible nombre en la lista: ")

if agenda["Nombre"] == nombre_busca:
    print("Ese nombre esta agendado")
else:
    print("Ese nombre no esta agendado")