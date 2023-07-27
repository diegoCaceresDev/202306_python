class Mascota:
    def __init__(self, nombre, tipo):
        self.nombre= nombre
        self.tipo= tipo
        self.golosinas = "dulces"
        self.salud= 20
        self.energia= 20
        
    def dormir(self):
        print(f"{self.nombre} esta durmiendo")
        self.energia += 25
        return self

    def comer(self):
        print(f"{self.nombre} esta comiendo")
        self.salud += 10
        self.energia += 5
        return self

        
    def jugando(self):
        print(f"{self.nombre} esta jugando")
        self.salud += 10
        return self


        
    def sonido(self):
        print(f"{self.nombre} esta rugiendo")

