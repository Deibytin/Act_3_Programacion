import math

class Rectangulo:

    def __init__(self, primera_esquina, esquina_diagonal_contraria):
        self.primera_esquina = primera_esquina
        self.esquina_diagonal_contraria = esquina_diagonal_contraria

    def calcular_perimetro(self):
        base = abs(self.esquina_diagonal_contraria.x - self.primera_esquina.x)
        altura = abs(self.esquina_diagonal_contraria.y - self.primera_esquina.y)
        perimetro = 2 * (base + altura)
        return perimetro

    def calcular_area(self):
        base = abs(self.esquina_diagonal_contraria.x - self.primera_esquina.x)
        altura = abs(self.esquina_diagonal_contraria.y - self.primera_esquina.y)
        area = base * altura
        return area

    def cuadrado(self):
        base = abs(self.esquina_diagonal_contraria.x - self.primera_esquina.x)
        altura = abs(self.esquina_diagonal_contraria.y - self.primera_esquina.y)
        return base == altura


class Punto:
    def __init__(self, c, d):
        self.c = c
        self.d = d

esquina_primera = Punto(7, -3)
esquina_contraria = Punto(1, 3)
rectangulo = Rectángulo(esquina_primera, esquina_contraria)

print("El perímetro es: ", rectangulo.calcular_perimetro())
print("El area es: ", rectangulo.calcular_area())
print("Es cuadrado?", rectangulo.cuadrado())
  


