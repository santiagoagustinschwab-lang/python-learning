class Banco:
    def __init__(self, nombre, saldo):
        self.nombre = nombre
        self.__saldo = saldo
        saldo == 0

    def cargar_saldo(self, carga):
        self.__saldo = self.__saldo + carga

    def ver_saldo(self):
        print(f"tu saldo es de {self.__saldo}")

    def retirar(self, monto):
        try:
            self.__saldo >= monto
            self.__saldo = self.__saldo - monto
        except:
            raise ValueError ("error")

