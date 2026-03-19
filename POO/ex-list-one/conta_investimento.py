# Classe Conta de Investimento
# Faça uma classe chamada contaInvestimento que seja semelhante à
# classe contaBancaria, com a diferença de que se adicione um atributo taxaJuros. Forneça um
# construtor que configure tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
# (sem parâmetro explícito) que adicione juros à conta. Escreva um programa que construa uma
# poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 10%. Depois aplique o método
# adicioneJuros() cinco vezes e imprime o saldo resultante.

class ContaInvestimento:
    def __init__(self, saldo_inicial, taxa_juros):
        self.saldo = saldo_inicial
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        juros = self.saldo * (self.taxa_juros / 100)
        self.saldo += juros
        print(f"Juros adicionados: R${juros:.2f}. Saldo atual: R${self.saldo:.2f}.")
