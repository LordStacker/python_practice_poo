#programacion orientada a objetos (POO OOP)

#Definir una clase (molde para crear mas objets de ese tipo
#(Coche) Con caracteristicas similares)

from typing import get_args


class Coche:

    #atributos o propiedades (variables)
    #Caracteristicas del coche
    color = "Rojo"
    marca = "Ferrari"
    modelo = "Aventador"
    velocidad = 300
    caballaje = 500
    plazas = 2

   #Metodos, son acciones que hace el objeto (coche) (funciones)
    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color
    def setModelo(self, modelo):
        self.modelo = modelo
    def getModelo (self):
        return self.modelo
    def acelerar(self):
        self.velocidad += 1
    def frenar(self):
        self.velocidad -= 1
    def getVelocidad(self):
        return self.velocidad
    def getfuelpercentage(self):
        pass
class lambo(Coche):
    tank_capacity = 50

    def setgas(self, gas):
        self.gas = gas
    def getfuelpercentage(self):
        return (self.gas*100)/(self.tank_capacity)

class Cybertruck(Coche):
    battery_capacity = 800
    def set_charge(self, battery):
        self.battery = battery
    def getfuelpercentage(self):
        return (self.battery*100)/(self.battery_capacity)


#fin definicion clase
print("Coche 1")
#Crear objeto / instaciar la clase
coche = Coche()
coche.setColor("Amarillo")
coche.setModelo("Murcielago")
print(coche.marca, coche.getModelo(), coche.getColor())
print("Velocidad actual: ", coche.velocidad)
#print("Velocidad actual: ", coche.getVelocidad())
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
#llamo al metodo al crearobjeto(PUNTO)y selecciono la accion.
print("Velocidad nueva: ", coche.velocidad)
#print("Velocidad nueva: ", coche.velocidad)

print("----------------------------")
#crear mas objetos
print("Coche 2 ")
coche2 = Coche()
coche2.setColor("Gris")
coche2.setModelo("Galliard")
print(coche2.marca ,coche2.getColor(), coche2.getModelo())