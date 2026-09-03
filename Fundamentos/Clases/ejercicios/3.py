class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area (self):
        area = 3.14 * self.radio ** 2
        print(f"El area del circulo cuyo radio es {self.radio}, es {area}")

circulo = Circulo(2)
circulo.calcular_area()