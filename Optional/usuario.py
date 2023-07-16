class Usuario:
    def __init__(self, name, ciudad="Encarnacion"):
        self.nombre = name
        self.ciudad = ciudad
        self.monto_cuenta = 0

    def hacer_deposito(self, monto):
        self.monto_cuenta += monto

    def hacer_retiro(self, monto):
        self.monto_cuenta -= monto

    def ver_balance(self):
        print(f"El saldo actual de {self.nombre} es de: ${self.monto_cuenta}")
        

def hacer_tranferencia(monto, cuenta_a_descontar, cuenta_a_aumentar):
    cuenta_a_descontar.hacer_retiro(monto)
    cuenta_a_aumentar.hacer_deposito(monto)


Usuario1 = Usuario("Diego Caceres", "Encarnacion")
Usuario2 = Usuario("Juan Perez", "Asuncion")
Usuario3 = Usuario("Pedro Gonzalez", "CDE")

Usuario1.hacer_deposito(100)
Usuario1.hacer_deposito(400)
Usuario1.hacer_deposito(150)
Usuario1.hacer_retiro(300)
Usuario1.ver_balance()

Usuario2.hacer_deposito(300)
Usuario2.hacer_deposito(500)
Usuario2.hacer_retiro(200)
Usuario2.hacer_retiro(300)
Usuario2.ver_balance()

Usuario3.hacer_deposito(1000)
Usuario3.hacer_retiro(100)
Usuario3.hacer_retiro(500)
Usuario3.hacer_retiro(400)
Usuario3.ver_balance()

print("-"*40)

hacer_tranferencia(150, Usuario1, Usuario3)
Usuario1.ver_balance()
Usuario3.ver_balance()

