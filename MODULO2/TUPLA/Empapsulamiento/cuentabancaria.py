


class CuentaBancaria:
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Consultar titular
    def ver_titular(self):
        return self.__titular

    # Consultar saldo
    def ver_saldo(self):
        return self.__saldo

    # Depositar dinero
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            print("Deposito realizado correctamente")
        else:
            print("El monto debe ser mayor a cero")

    # Retirar dinero
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            print("Retiro realizado correctamente")
        else:
            print("No se puede retirar")


# Crear cuenta bancaria
c = CuentaBancaria("Ana", 100)

print(c.ver_titular(), c.ver_saldo())

c.depositar(50)
print(c.ver_titular(), c.ver_saldo())

c.retirar(500)
print(c.ver_titular(), c.ver_saldo())
