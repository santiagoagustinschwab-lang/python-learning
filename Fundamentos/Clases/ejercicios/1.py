#1
class producto:
    def __init__(self, nombre, precio):
        self.price = precio
        self.name = nombre
        self.product = nombre, precio

producto_estrella = producto("auriculares", 200)
print(producto_estrella.product)