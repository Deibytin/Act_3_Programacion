import math

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def mostrar(self):
        print("Coordenadas del punto: ",(self.x, self.y))

    def mover(self, a, b):
        self.x= a
        self.y= b

    def calcular_distancia(self, otro_punto):
        distancia = math.sqrt((otro_punto.x - self.x)**2 + (otro_punto.y - self.y)**2)
        return distancia

punto1 = Punto(2, 1)
punto1.mostrar()

punto1.mover(4,-6)
print("El punto despues de haber sido movido: ")
punto1.mostrar()
    
punto2= Punto(8,9)

distancia= punto1.calcular_distancia(punto2)
print("La distancia entre el punto1 y el punto2", distancia )