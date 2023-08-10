from cuenta_bancaria import CuentaBancaria

class Usuario:
    def __init__(self, name, ciudad="Encarnacion"):
        self.nombre = name
        self.ciudad = ciudad
        self.monto_cuenta = CuentaBancaria(0)

    def hacer_deposito(self, monto):
        self.monto_cuenta.deposito(monto)
        return self

    def hacer_retiro(self, monto):
        self.monto_cuenta.retiro(monto)
        return self


    def ver_balance(self):
        self.monto_cuenta.mostrar_info_cuenta()
        return self


user1 = Usuario("Diego Caceres", "Encarnacion")

user1.hacer_deposito(1000).hacer_retiro(500).ver_balance().hacer_deposito(1000).ver_balance()