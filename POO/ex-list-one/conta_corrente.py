# Classe Conta Corrente:
# Crie uma classe para implementar uma conta
# corrente. A classe deve possuir os seguintes
# atributos: número da conta, nome do correntista
# e saldo. Os métodos são osseguintes: alterarNome,
# depósito e saque. No construtor, saldo é
# opcional, com valor default zero e os demais
# atributos são obrigatórios.

class Conta():
    def __init__(self, numeroConta, nomeCorrentista, saldo=0.0):
        self.numeroConta = numeroConta
        self.nomeCorrentista = nomeCorrentista
        self.saldo = saldo

    def alterarNome(self, novoNome="N/D"):
        self.nomeCorrentista = novoNome

    def depositar(self, adicaoSaldo=0.0):
        self.saldo = self.saldo + adicaoSaldo

    def saque(self, reducaoSaldo=0.0):
        self.saldo = self.saldo - reducaoSaldo
