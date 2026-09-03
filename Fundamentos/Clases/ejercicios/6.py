#6
class Banco:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo
        saldo == 0

    def cargar_saldo(self, carga):
        self.__saldo = self.__saldo + carga

    def ver_saldo(self):
        print(f"tu saldo es de {self.__saldo}")

mi_cuenta = Banco("Santiago", 0)
mi_cuenta.cargar_saldo(500)
mi_cuenta.ver_saldo()

mi_cuenta.cargar_saldo(300)
mi_cuenta.ver_saldo()