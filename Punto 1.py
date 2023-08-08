class Vehículo:
    def __init__(self, velo_max, km):
        self.velo_max = velo_max
        self.km = km

carro = Vehículo(300, 5000)
print(f"Velocidad máxima del carro: {carro.velo_max} km/h")
print(f"Kilometraje del carro: {carro.km} km")