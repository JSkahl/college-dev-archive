# Classe TV
# Faça um programa que simule um televisor
# criando-o como um objeto. O usuário deve
# ser capaz de informar o número do canal e
# aumentar ou diminuir o volume. Certifique-se
# de que o número do canal e o nível do volume
# permanecem dentro de faixas válidas.

class Televisor():
    # Faixa válida de canal: 0-50
    # Faixa válida de som: 0-100
    def __init__(self, canal=0, som=50):
        self.canal = canal
        self.som = som

    def alterarCanal(self, operacao):
        operacoesValidas = ["começo", "fim", "incrementar", "decrementar"]

        if self.canal >= 0 and self.canal <= 50:
            if operacao in operacoesValidas:
                match operacao:
                    case "começo":
                        self.canal = 0
                    case "fim":
                        self.canal = 50
                    case "incrementar":
                        self.canal++
                    case "decrementar":
                        self.canal--
                    case _:
                        print("Operação não informada")
        else:
            print("Canal não existente")

    def alterarSom(self, operacao):
        operacoesValidas = ["mutar", "incrementar", "decrementar"]

        if self.som >= 0 and self.som <= 100:
            if operacao in operacoesValidas:
                match operacao:
                    case "mutar":
                        self.mutar = 0
                    case "incrementar":
                        self.mutar++
                    case "decrementar":
                        self.mutar--
                    case _:
                        print("Operação não informada")
        else:
            print("Som máximo/mínimo atingido")
