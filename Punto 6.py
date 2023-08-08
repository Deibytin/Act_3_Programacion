class Carta:
    PINTA_CORAZON = "Corazón"
    PINTA_PICA = "Pica"
    PINTA_TREBOL = "Trébol"
    PINTA_DIAMANTE = "Diamante"

    def __init__(self, valor, pinta):
        self.valor = valor
        self.pinta = pinta


carta1 = Carta(5, Carta.PINTA_CORAZON)
carta2 = Carta(3, Carta.PINTA_DIAMANTE)

print("Carta 1: Valor = ", carta1.valor, "  Pinta = ", carta1.pinta)
print("Carta 2: Valor = ", carta2.valor, "  .Pinta = ", carta2.pinta)