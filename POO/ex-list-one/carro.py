# Classe Carro
# Implemente uma classe chamada Carro com as seguintes propriedades:
# a. Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa
#    quantidade de combustível no tanque.
# b. O consumo é especificado no construtor e o nível de combustível inicial é 0.
# c. Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância,
#    reduzindo o nível de combustível no tanque de gasolina.
# d. Forneça um método obterGasolina( ), que retorna o nível atual de combustível.
# e. Forneça um método adicionarGasolina( ), para abastecer o tanque.

class Carro:
    def __init__(self, consumo_km_por_litro):
        self.consumo_km_por_litro = consumo_km_por_litro
        self.nivel_combustivel = 0.0

    def andar(self, distancia_km):
        litros_necessarios = distancia_km / self.consumo_km_por_litro
        if litros_necessarios > self.nivel_combustivel:
            print("Combustível insuficiente para percorrer a distância.")
            return
        self.nivel_combustivel -= litros_necessarios
        print(f"Você percorreu {distancia_km} km e consumiu {litros_necessarios:.2f} litros de combustível.")

    def obter_gasolina(self):
        return self.nivel_combustivel

    def adicionar_gasolina(self, litros):
        self.nivel_combustivel += litros
        print(f"Adicionado {litros:.2f} litros de combustível. Nível atual: {self.nivel_combustivel:.2f} litros.")
