# Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado
# e calcular Área;

class Quadrado():
    def __init__(self, tamanhoLado=0.0):
        self.tamanhoLado = tamanhoLado

    def mudaValorLado(self, novoTamanhoLado):
        self.tamanhoLado = novoTamanhoLado

    def mostraValorLado(self):
        return f"Tamanho do lado: {self.tamanhoLado}"

    def calculaArea(self):
        areaQuadrado = self.tamanhoLado ** 2

        return f"A área do quadrado é {areaQuadrado}"
