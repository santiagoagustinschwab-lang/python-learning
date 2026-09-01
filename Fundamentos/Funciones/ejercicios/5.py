#5
def contar_vocales (palabra):
    vocales = "aeiou"
    contador = 0
    for letra in palabra:
        if letra in vocales:
            contador += 1
    return contador

print(contar_vocales("hola")) 