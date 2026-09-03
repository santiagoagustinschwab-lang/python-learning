#9
class producto:
    def __init__(self, nombre, precio):
        self.price = precio
        self.name = nombre
        self.product = nombre, precio

    def mostrar_info(self):
        print(self.product)

producto_1 = producto("auriculares", 100)
producto_2 = producto("mouse", 200)
producto_3 = producto("teclado", 300)

lista_de_productos = [producto_1, producto_2, producto_3]

for productos in lista_de_productos:
    productos.mostrar_info()