# Crie uma classe chamada Robo(). Ela deverá
# ter duas propriedades privadas: nome e
# ano_construcao. Também deverá ter um método
# de nome “diga_alo()”, para mostrar na tela
# o nome do robô e seu ano de construção.
# Crie os métodos “setters” e “getters”
# necessários. Instancie a classe e use os
# métodos criados para visualizar / atualizar
# os dados.

# Exercício de codificação

class Robo():
    def __init__(self, nome="", ano_construcao=0):
        self.__nome = nome
        self.__ano_construcao= ano_construcao

    def setRobo(self, nome, ano_construcao):
        self.__nome = nome
        self.__ano_construcao = ano_construcao

    def getRobo(self):
        return f"Robo\n==========\n{self.__nome}\n{self.__ano_construcao}"

    def diga_algo(self):
        return f"O Robô {self.__nome} foi criado no ano {self.__ano_construcao}." 

robo1 = Robo()
robo1.setRobo("Siri", 2010)
print(robo1.diga_algo())
print(robo1.getRobo())
