#10
libro_1 = {
    "titulo":"Cien años de soledad",
    "autor":"Garcia Marquez",
    "año":1967,
}

libro_2 = {
    "titulo":"1984",
    "autor":"George Orwell",
    "año":1949,
}

libro_3 = {
    "titulo":"El principito",
    "autor":"saint",
    "año":1943,
}

lista = [libro_1, libro_2, libro_3]

comprovacion = input("Ingrese algun titulo: ")
print(comprovacion == lista[0]["titulo"] or comprovacion == lista[1]["titulo"] or comprovacion == lista[2]["titulo"])
