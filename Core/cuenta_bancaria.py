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


cuenta1 = CuentaBancaria()
cuenta2 = CuentaBancaria()


if __name__ == "__main__":
    cuenta1.deposito(500).deposito(300).deposito(400).retiro(250).generar_interés().mostrar_info_cuenta()

    cuenta2.deposito(800).deposito(1000).retiro(100).retiro(500).retiro(300).retiro(200).mostrar_info_cuenta()

    CuentaBancaria.mostrar_instancias()

