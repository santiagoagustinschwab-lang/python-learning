#8
netflix = {
    "descripcion":"servicio de streaming",
    "valor":100,
}

spotify = {
    "descripcion":"servicio de musica",
    "valor":200,
}

youtube = {
    "descripcion":"servicio de streaming",
    "valor":150,
}


lista = [netflix, spotify, youtube]

gasto_total = lista[0]["valor"] + lista[1]["valor"] + lista[2]["valor"]
print(gasto_total)