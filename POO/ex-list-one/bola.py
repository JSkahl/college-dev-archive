# Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola():
    def __init__(self, cor="N/D", circunferencia=0.0, material="N/D"):
        self.cor = cor 
        self.circunferencia = circunferencia
        self.material = material


    def trocaCor(self, novaCor):
        self.cor = novaCor

    def mostrarCor(self):
        return f"Cor: {self.cor}"
