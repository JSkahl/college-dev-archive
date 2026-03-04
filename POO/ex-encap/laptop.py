# Implemente uma classe chamada Laptop que possua
# um atributo privado chamado “preco” que
# armazena o preço do laptop (sem qualquer
# validação). Em seguida, implemente um método
# para ler esse atributo chamado “get_preco()”
# e um método para modificar esse atributo chamado
# “set_preco()” sem validação também. Em seguida,
# crie uma instância da classe Laptop siga estas
# etapas:
# - usando o método “get_preco()” imprima o valor do atributo “preco” na tela
# - usando o método “set_preco()”, defina o valor do atributo “preco” para 3999”

# Exercício de codificação

class Laptop():
    def __init__(self, preco=0):
        self.preco = preco

    def setPreco(self, preco):
        self.preco = preco

    def getPreco(self):
        return f"O preço do Laptop é de R${self.preco}."

laptop1 = Laptop(1500)
print(laptop1.getPreco())

laptop1.setPreco(2500)
print(laptop1.getPreco())
