# Implemente uma classe chamada Pessoa que tenha
# dois atributos privados chamados “primeiroNome”
# e “ultimoNome”, respectivamente. Em seguida,
# implemente métodos chamados “getPrimeiroNome()”
# e “getUltimoNome()”, para ler os atributos, e
# os métodos “setPrimeiroNome()” e 
# “setUltimoNome()” para atribuir valores a eles.
# Depois crie uma instância da classe Pessoa
# definindo os seguintes valores:
# primeiroNome = 'João'
# ultimoNome = 'Carvalho'
#
# Após, imprima os valores desses atributos no
# console.

# Exercício de codificação

class Pessoa():
    def __init__(self, primeiroNome="", ultimoNome=""):
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def setUltimoNome(self, ultimoNome):
        self.__ultimoNome = ultimoNome

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def getUltimoNome(self):
        return self.__ultimoNome

pessoa1 = Pessoa()
pessoa1.setPrimeiroNome("João")
pessoa1.setUltimoNome("Carvalho")
print(pessoa1.getPrimeiroNome())
print(pessoa1.getUltimoNome())
