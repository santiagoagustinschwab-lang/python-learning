#5
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.datos = nombre, edad

    def cumplir_años(self, cantidad):
        return self.edad + cantidad

mi_persona = Persona("Santiago", 17)
print(mi_persona.cumplir_años(1))
