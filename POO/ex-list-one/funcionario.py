# Classe Funcionário
# Implemente a classe Funcionário. Um empregado tem um nome (um string) e
# um salário(um double). Escreva um construtor com dois parâmetros (nome e salário) e métodos para
# devolver nome e salário. Escreva um pequeno programa que teste sua classe.
# Aprimore a classe do exercício anterior para adicionar o método aumentarSalario
# (porcentualDeAumento) que aumente o salário do funcionário em uma certa porcentagem.

class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def obter_nome(self):
        return self.nome

    def obter_salario(self):
        return self.salario

    def aumentar_salario(self, percentual_de_aumento):
        aumento = self.salario * (percentual_de_aumento / 100)
        self.salario += aumento
        print(f"Salário aumentado em {percentual_de_aumento}%. Novo salário: R${self.salario:.2f}.")
