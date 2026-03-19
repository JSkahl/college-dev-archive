# Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: envelhecer, engordar, emagrecer, crescer.
#
# Obs: Por padrão, a cada ano que nossa pessoa
# envelhece, sendo a idade dela menor que 21 anos, ela
# deve crescer 0,5 cm.

class Pessoa():
    def __init__(self, nome="", idade=0, peso=0.0, altura=0.0):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, quantidadeAnos):
        if self.idade < 21:
            alturaACrescer = quantidadeAnos * 0.5 

            self.altura = self.altura + alturaACrescer

        self.idade = self.idade + quantidadeAnos

    def engordar(self, quantidadePeso):
        self.peso = self.peso + quantidadePeso

    def emagrecer(self, quantidadePeso):
        self.peso = self.peso - quantidadePeso

    def crescer(self, quantidadeAnos):
        self.altura = self.altura + quantidadeAnos
