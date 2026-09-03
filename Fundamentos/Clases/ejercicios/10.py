class Contacto:
    def __init__(self, nombre, telefono, ciudad):
        self.nombre = nombre
        self.telefono = telefono
        self.ciudad = ciudad

contacto_1 = Contacto("Santiago", "1", "mg",)
contacto_2 = Contacto("Ricardo", "2", "temp",)
contacto_3 = Contacto("Laura", "3", "lavall",)

agenda = [contacto_1, contacto_2, contacto_3]

def buscar_contacto(lista, nombre):
    for contacto in lista:
        if contacto.nombre == nombre:
            return contacto

resultado = buscar_contacto(agenda, "Santiago")
print(resultado.nombre, resultado.telefono, resultado.ciudad)