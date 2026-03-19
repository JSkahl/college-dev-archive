# Classe Bomba de Combustível
# Faça um programa completo utilizando classes e métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
#   i. tipoCombustivel.
#   ii. valorLitro
#   iii. quantidadeCombustivel
# b. Possua no mínimo esses métodos:
#   i. abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a
#      quantidade de litros que foi colocada no veículo
#   ii. abastecerPorLitro( ) – método onde é informado a quantidade em litros de
#       combustível e mostra o valor a ser pago pelo cliente.
#   iii. alterarValor( ) – altera o valor do litro do combustível.
#   iv. alterarCombustivel( ) – altera o tipo do combustível.
#   v. alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na
#      bomba.
#
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

class BombaCombustivel:
    def __init__(self, tipo_combustivel, valor_litro, quantidade_combustivel):
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.quantidade_combustivel = quantidade_combustivel

    def abastecer_por_valor(self, valor):
        litros_abastecidos = valor / self.valor_litro
        if litros_abastecidos > self.quantidade_combustivel:
            print("Quantidade insuficiente na bomba.")
            return
        self.quantidade_combustivel -= litros_abastecidos
        print(f"Abastecido {litros_abastecidos:.2f} litros por R${valor:.2f}.")

    def abastecer_por_litro(self, litros):
        valor_a_pagar = litros * self.valor_litro
        if litros > self.quantidade_combustivel:
            print("Quantidade insuficiente na bomba.")
            return
        self.quantidade_combustivel -= litros
        print(f"Abastecido {litros:.2f} litros por R${valor_a_pagar:.2f}.")

    def alterar_valor(self, novo_valor):
        self.valor_litro = novo_valor
        print(f"Valor do litro alterado para R${novo_valor:.2f}.")

    def alterar_combustivel(self, novo_tipo):
        self.tipo_combustivel = novo_tipo
        print(f"Tipo de combustível alterado para {novo_tipo}.")

    def alterar_quantidade_combustivel(self, nova_quantidade):
        self.quantidade_combustivel = nova_quantidade
        print(f"Quantidade de combustível alterada para {nova_quantidade:.2f} litros.")
