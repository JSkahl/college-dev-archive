# Classe Retangulo: Crie uma classe que modele um retangulo:
#
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou
# Base e Altura, a escolher)
#
# b. Métodos: Mudar valor dos lados, Retornar valor dos
# lados, calcular Área e calcular Perímetro;
#
# c. Crie um programa que utilize esta classe. Ele deve
# pedir ao usuário que informe as medidades de um local.
#
# Depois, deve criar um objeto com as medidas e calcular
# a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo():
    def __init__(self, base=0.0, altura=0.0):
        self.base = base
        self.altura = altura

    def mudaValor(self, lado="", valor=0.0):
        ladosPermitidos=["base", "altura"]

        if lado in ladosPermitidos:
            self.lado = valor
        else: 
            print("Valor não permitido")

    def mostraValores(self):
        return f"Base: {self.base}\nAltura: {self.altura}"

    def calculaArea(self):
        # base x altura
        areaRetangulo = self.base * self.altura

        return f"A área do retângulo é: {areaRetangulo}"

    def calculaPerimetro(self):
        # 2 * (base + altura)
        perimetroRetangulo = 2 * (self.base + self.altura)

        return f"O perímetro do retângulo é: {perimetroRetangulo}"

print("===========================")
print("= Calculo de um retangulo =")
print("===========================")

base = input("\nInsira a base do retângulo: ")
altura = input("\nInsira a altura do retângulo: ")
print("")

retangulo = Retangulo(float(base), float(altura))

print(retangulo.calculaArea())
print(retangulo.calculaPerimetro())

# Sem as medidas do piso e do rodapé não há como concluir o código.
