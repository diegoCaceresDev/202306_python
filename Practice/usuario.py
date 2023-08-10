

class Usuario:
    def __init__(self, name, ciudad="Encarnacion"):
        self.nombre = name
        self.ciudad = ciudad
        self.monto_cuenta = 0

    def hacer_deposito(self, monto):
        self.monto_cuenta.deposito(monto)
        return self

    def hacer_retiro(self, monto):
        self.monto_cuenta.retiro(monto)
        return self


    def ver_balance(self):
        self.monto_cuenta.mostrar_info_cuenta()
        return self


def hacer_tranferencia(monto, cuenta_a_descontar, cuenta_a_aumentar):
    cuenta_a_descontar.hacer_retiro(monto)
    cuenta_a_aumentar.hacer_deposito(monto)


Usuario1 = Usuario("Diego Caceres", "Encarnacion")
Usuario2 = Usuario("Juan Perez", "Asuncion")
Usuario3 = Usuario("Pedro Gonzalez", "CDE")

Usuario1.hacer_deposito(100).hacer_deposito(400).hacer_deposito(150).hacer_retiro(300).ver_balance()

Usuario2.hacer_deposito(300).hacer_deposito(500).hacer_retiro(200).hacer_retiro(300).ver_balance()

Usuario3.hacer_deposito(1000).hacer_retiro(100).hacer_retiro(500).hacer_retiro(400).ver_balance()

print("-"*40)

hacer_tranferencia(150, Usuario1, Usuario3)
Usuario1.ver_balance()
Usuario3.ver_balance()

