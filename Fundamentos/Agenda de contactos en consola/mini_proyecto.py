nombre_1 = input("Ingrese el nombre del contacto: ")
telefono_1 = int(input("Ingrese el telefono: "))
ciudad_1 = input("Ingrese la ciudad: ")

nombre_2 = input("Ingrese el nombre del contacto: ")
telefono_2 = int(input("Ingrese el telefono: "))
ciudad_2 = input("Ingrese la ciudad: ")

contacto_1 = {
    "Nombre":nombre_1,
    "Telefono":telefono_1,
    "Ciudad":ciudad_1,
}

contacto_2 = {
    "Nombre":nombre_2,
    "Telefono":telefono_2,
    "Ciudad":ciudad_2,
}

agenda = [contacto_1, contacto_2]

print("CONTACTO 1")
print("Los datos del primer contacto son:", agenda[0]["Nombre"], agenda[0]["Telefono"], agenda[0]["Ciudad"])
print("CONTACTO 2")
print("Los datos del primesegundo contacto son:", agenda[1]["Nombre"], agenda[1]["Telefono"], agenda[1]["Ciudad"])

nombre_buscado = input("Que nombre buscas?: ")
print(nombre_buscado == contacto_1["Nombre"])