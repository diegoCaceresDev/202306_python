from mascota import Mascota

class Ninja():
    def __init__(self, nombre, apellido, mascota, premio, comida):
        self.nombre= nombre
        self.apellido= apellido
        self.mascotas= mascota
        self.premio= premio
        self.comida_mascota= comida
    
    def caminar(self):
        print(f"{self.nombre} caminando")
        self.mascotas.jugando()
        return self
        
    def alimentar(self):
        print(f"{self.nombre} alimentando a {self.mascotas.nombre}")
        self.mascotas.comer()
        return self

    def bañar(self):
        print(f"{self.nombre} bañando a {self.mascotas.nombre}")
        self.mascotas.sonido
        return self

kurama = Mascota("Kurama", "Legendario")
ninja = Ninja("Naruto", "Uzumaki", kurama, "Caramelo", "Ramen")



ninja.caminar().alimentar().bañar()