import math

class Punto:
    def __init__(self, e, f):
        self.e = e
        self.f = f

class Circulo:
    def __init__(self, centro, radio):
        self.centro = centro
        self.radio = radio
    
    def calcular_area(self):
        area = math.pi * self.radio**2
        return area
    
    def calcular_perimetro(self):
        perimetro = 2 * math.pi * self.radio
        return perimetro
    
    def punto_pertenece_al_circulo(self, punto):
        distancia_centro_a_punto = (math.sqrt((punto.e - self.centro.e)**2 + (punto.f - self.centro.f)**2))
        return distancia_centro_a_punto <= self.radio
  
centro = Punto(7, 15)
circulo = Circulo(centro, 12)

print("El area del circulo es: ", circulo.calcular_area())
print("el perímetro del circulo es: ", circulo.calcular_perimetro())

punto1 = Punto(1, 3)
punto2 = Punto(4, 5)

print("¿punto 1 pertenece al círculo?", circulo.punto_pertenece_al_circulo(punto1))
print("¿punto 2 pertenece al círculo?", circulo.punto_pertenece_al_circulo(punto2))

