# Crie uma classe chamada Empregado(), com
# três propriedades: nome, salario (deve ser
# privada) e projeto. Ela também possui um
# método chamado “trabalho()”, que deverá
# imprimir o nome do funcionário e o projeto
# em que ele está trabalhando e um outro método
# chamado “mostrar()” para exibir os detalhes
# desse empregado (i.e. nome e salário). Atente
# para o modificador de acesso da propriedade
# “salario”. Use o método adequado para ter
# acesso a ela. Crie um objeto desta classe
# (i.e. instância) e use os métodos
# para visualizar os dados.

# Exercício de codificação

class Empregado():
    def __init__(self, nome="", salario=0, projeto=""):
        self.__nome = nome
        self.__salario = salario
        self.projeto = projeto

    def setEmpregado(self, nome, salario, projeto):
        self.__nome = nome
        self.__salario = salario
        self.projeto = projeto

    def trabalho(self):
        return f"O empregado {self.__nome} está no projeto {self.projeto}."

    def mostrar(self):
        return f"EMPREGADO\n===========\nNome: {self.__nome}\nSalário: {self.__salario}\nProjeto: {self.projeto}"

empregado1 = Empregado()
empregado1.setEmpregado("Daniel", 5000, "Dominar a lua")

print(empregado1.trabalho())
print(empregado1.mostrar())
