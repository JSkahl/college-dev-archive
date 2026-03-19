# Classe Bichinho Virtual
# Crie uma classe que modele um Tamagushi
# (Bichinho Eletrônico):
# a. Atributos: Nome, Fome, Saúde e Idade
# b. Métodos: Alterar Nome, Fome, Saúde e
# Idade; Retornar Nome, Fome, Saúde e Idade
#
# Obs: Existe mais uma informação que devemos
# levar em consideração, o Humor do nosso
# tamagushi, este humor é uma combinação
# entre os atributos Fome e Saúde, ou seja,
# um campo calculado, então não devemos criar
# um atributo para armazenar esta informação
# por que ela pode ser calculada a qualquer
# momento.


class Pet():
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

        self.humor = self.saude / self.fome

    def editarInformacao(self, informacaoParaAlterar, informacaoNova):
        informacoesValidas = ["nome", "fome", "saude", "idade"]

        if informacaoParaAlterar in informacoesValidas:
            match informacaoParaAlterar:
                case "nome":
                    self.nome = informacaoNova
                case "fome":
                    self.fome = informacaoNova
                case "saude":
                    self.saude = informacaoNova
                case "idade":
                    self.idade = informacaoNova
                case _:
                    print("Informação não existente no sistema")

    def retornarInformacao(self, informacaoParaRetornar):
        informacoesValidas = ["nome", "fome", "saude", "idade"]

        if informacaoParaRetornar in informacoesValidas:
            match informacaoParaRetornar:
                case "nome":
                    return self.nome
                case "fome":
                    return self.fome
                case "saude":
                    return self.saude
                case "idade":
                    return self.idade
                case _:
                    print("Informação não existente no sistema")

    # Classe Bichinho Virtual++:
    # Melhore o programa do bichinho virtual, permitindo que o usuário
    # especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
    # Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida * 2
        if self.fome < 0:
            self.fome = 0
        print(f"{self.nome} foi alimentado com {quantidade_comida} unidades de comida. Fome atual: {self.fome}.")

    def brincar(self, tempo_brincadeira):
        self.saude += tempo_brincadeira * 3
        if self.saude > 100:
            self.saude = 100
        print(f"{self.nome} brincou por {tempo_brincadeira} minutos. Saúde atual: {self.saude}.")


# Crie uma Fazenda de Bichinhos instanciando vários objetos bichinho e mantendo o controle deles
# através de uma lista. Imite o funcionamento do programa básico, mas ao invés de exigir que o usuário
# tome conta de um único bichinho, exija que ele tome conta da fazenda inteira. Cada opção do menu
# deveria permitir que o usuário executasse uma ação para todos os bichinhos (alimentar todos os
# bichinhos, brincar com todos os bichinhos, ou ouvir a todos os bichinhos). Para tornar o programa
# mais interessante, dê para cada bichinho um nível inicial aleatório de fome e tédio.

def criarFazendaDeBichinhos():
    import random

    fazenda = []
    for i in range(5):
        nome = f"Bichinho{i+1}"
        fome = random.randint(0, 100)
        saude = random.randint(0, 100)
        idade = random.randint(1, 10)
        bichinho = Pet(nome, fome, saude, idade)
        fazenda.append(bichinho)

    return fazenda

def mostrarMenu():
    print("Menu:")
    print("1. Alimentar todos os bichinhos")
    print("2. Brincar com todos os bichinhos")
    print("3. Ver status de todos os bichinhos")
    print("4. Sair")


fazenda = criarFazendaDeBichinhos()
mostrarMenu()
escolha = input("Escolha uma opção: ")

if escolha == "1":
    quantidade_comida = int(input("Quanto de comida deseja fornecer para cada bichinho? "))
    for bichinho in fazenda:
        bichinho.alimentar(quantidade_comida)
elif escolha == "2":
    tempo_brincadeira = int(input("Por quanto tempo deseja brincar com cada bichinho? "))
    for bichinho in fazenda:
        bichinho.brincar(tempo_brincadeira)
elif escolha == "3":
    for bichinho in fazenda:
        print(f"Status de {bichinho.nome}: Fome: {bichinho.fome}, Saúde: {bichinho.saude}, Idade: {bichinho.idade}, Humor: {bichinho.humor:.2f}")
elif escolha == "4":
    print("Saindo do programa...")
    break
else:
    print("Opção inválida. Tente novamente.")
