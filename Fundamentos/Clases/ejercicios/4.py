#4
class Perro:
    def __init__(self, nombre, raza = "generica"):
        self.nombre = nombre
        self.raza = raza
        self.rope = nombre, raza

mi_perro = Perro("lola", "schnawser")
print(mi_perro.rope)