# Classe Bichinho Virtual++:
# Melhore o programa do bichinho virtual, permitindo que o usuário
# especifique quanto de comida ele fornece ao bichinho e por quanto tempo ele brinca com o bichinho.
# Faça com que estes valores afetem quão rapidamente os níveis de fome e tédio caem.

class Pet:
    def __init__(self, nome):
        self.nome = nome
        self.fome = 50
        self.tedio = 50

    def alimentar(self, quantidade_comida):
        self.fome -= quantidade_comida * 2  # Quanto mais comida, mais rápido a fome diminui
        if self.fome < 0:
            self.fome = 0
        print(f"{self.nome} foi alimentado com {quantidade_comida} unidades de comida. Fome atual: {self.fome}.")

    def brincar(self, tempo_brincadeira):
        self.tedio -= tempo_brincadeira * 3  # Quanto mais tempo brincando, mais rápido o tédio diminui
        if self.tedio < 0:
            self.tedio = 0
        print(f"{self.nome} brincou por {tempo_brincadeira} minutos. Tédio atual: {self.tedio}.")

    def status(self):
        print(f"Status de {self.nome}: Fome: {self.fome}, Tédio: {self.tedio}.")
