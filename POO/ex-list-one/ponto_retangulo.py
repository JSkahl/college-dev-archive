# Classe Ponto e Retangulo
# Faça um programa completo utilizando funções e classes que:
# a. Possua uma classe chamada Ponto, com os atributos x e y.
# b. Possua uma classe chamada Retangulo, com os atributos largura e altura.
# c. Possua uma função para imprimir os valores da classe Ponto
# d. Possua uma função para encontrar o centro de um Retângulo.
# e. Você deve criar alguns objetos da classe Retangulo.
# f. Cada objeto deve ter um vértice de partida, por exemplo, o vértice inferior esquerdo do
# retângulo, que deve ser um objeto da classe Ponto.
# g. A função para encontrar o centro do retângulo deve retornar o valor para um objeto do tipo
# ponto que indique os valores de x e y para o centro do objeto.
# h. O valor do centro do objeto deve ser mostrado na tela
# i. Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.

class Ponto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def imprimir(self):
        print(f"Ponto: ({self.x}, {self.y})")

class Retangulo:
    def __init__(self, largura=0, altura=0, vertice_inferior_esquerdo=None):
        self.largura = largura
        self.altura = altura
        self.vertice_inferior_esquerdo = vertice_inferior_esquerdo or Ponto()

    def centro(self):
        centro_x = self.vertice_inferior_esquerdo.x + self.largura / 2
        centro_y = self.vertice_inferior_esquerdo.y + self.altura / 2
        return Ponto(centro_x, centro_y)

def menu():
    retangulo = Retangulo()
    while True:
        print("\nMenu:")
        print("1. Definir retângulo")
        print("2. Imprimir centro do retângulo")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            largura = float(input("Digite a largura do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))
            x = float(input("Digite a coordenada x do vértice inferior esquerdo: "))
            y = float(input("Digite a coordenada y do vértice inferior esquerdo: "))
            retangulo = Retangulo(largura, altura, Ponto(x, y))
        elif escolha == '2':
            centro = retangulo.centro()
            print(f"Centro do retângulo: ({centro.x}, {centro.y})")
        elif escolha == '3':
            break
        else:
            print("Opção inválida. Tente novamente.")
