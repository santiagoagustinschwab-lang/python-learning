#8
class Libro:
    def __init__(self,titulo, autor, leido = False):
        self.titulo = titulo
        self.autor = autor
        self.leido = leido

    def marcar_leido(self):
        self.leido = True

mi_libro = Libro("libro x", "autor x")

mi_libro.marcar_leido()
print(mi_libro.leido)