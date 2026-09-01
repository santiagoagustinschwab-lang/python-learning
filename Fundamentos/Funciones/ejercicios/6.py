contacto_1 = {
    "Nombre":"santiago",
    "Apellido":"schwab",
    }
contacto_2 = {
    "Nombre":"ricardo",
    "Apellido":"schwab",
    }

agenda = [contacto_1, contacto_2]

def buscar_contacto(agenda, nombre):
    for contacto in agenda:
        if contacto["Nombre"] == nombre:
            return contacto

print(buscar_contacto(agenda, "santiago"))