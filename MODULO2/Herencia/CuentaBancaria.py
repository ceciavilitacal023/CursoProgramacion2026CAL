

class CuentaBancaria:
    # Constructor
    def __init__(self, titular, saldo):
        self.__titular = titular
        self.__saldo = saldo

    # Metodo para depositar
    def depositar(self, monto):
        self.__saldo += monto
        print("Deposito realizado:", monto)

    # Metodo para retirar
    def retirar(self, monto):
        if monto <= self.__saldo:
            self.__saldo -= monto
            print("Retiro realizado:", monto)
        else:
            print("Saldo insuficiente")

    # Metodo para consultar saldo
    def ver_saldo(self):
        return self.__saldo

    # Metodo para mostrar informacion
    def mostrar(self):
        print("Titular:", self.__titular)
        print("Saldo:", self.__saldo)


# Clase hija
class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo, tasa):
        super().__init__(titular, saldo)

        # Atributo propio
        self.__tasa = tasa

    # Metodo para aplicar intereses
    def aplicar_interes(self):
        interes = self.ver_saldo() * self.__tasa / 100
        self.depositar(interes)

        print("Interes generado:", interes)
        print("Nuevo saldo:", self.ver_saldo())

    def mostrar(self):
        super().mostrar()
        print("Tasa de interes:", self.__tasa, "%")

# Crear objeto
ahorro = CuentaAhorro("Pedro", 1000, 5)

print("----- CUENTA DE AHORRO -----")
ahorro.mostrar()

print("----------------------------")
ahorro.depositar(500)

print("----------------------------")
ahorro.retirar(200)

print("----------------------------")
ahorro.aplicar_interes()