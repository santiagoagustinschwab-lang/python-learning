#2
class producto:
    def __init__(self, nombre, precio):
        self.price = precio
        self.name = nombre
        self.product = nombre, precio

    def mostrar_info (self):
        print(f"el producto {self.name} vale {self.price}")

producto_final = producto("auriculares", 200)
producto_final.mostrar_info()