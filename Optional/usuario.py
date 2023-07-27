# from Core.cuenta_bancaria import CuentaBancaria no funciona // TODO

class CuentaBancaria:
    
    instancias = []
    
    def __init__(self, balance_inicial = 0, interes_inicial = 0.01):
        self.balance = balance_inicial
        self.interes = interes_inicial
        self.instancias.append(self)
    
    def deposito(self, amount):
        self.balance += amount
        return self
    
    def retiro(self, amount):
        
        if(self.balance < amount):
            print("Fondos insuficientes")
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self

    def mostrar_info_cuenta(self):
        
        print(f"Balance: {self.balance}")
        return self

    
    def generar_interés(self):
        interes = self.balance * self.interes
        self.balance += interes
        return self
    

    @classmethod    
    def mostrar_instancias(cls):
        for instancia in cls.instancias:
            print(instancia)


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

