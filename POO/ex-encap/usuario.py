# Programação Orientada a Objetos

# Esse arquivo contém as respostas das questões
# prática da atividade sobre encapsulamento, referente a classe
# de Programação Orientada à Objetos, mestrada
# pelo Professor Paulo César.

# O arquivo '.md', neste mesmo diretório,
# possuí as respostas para a parte, de fato,
# prática da atividade.


# Questões

# Exercício de codificação

# Vamos voltar para a classe Usuario que
# desenvolvemos nas atividades anteriores.
# Agora vamos definir o primeiroNome do
# usuário como uma propriedade privada (private).
# Esta é a classe Usuario:

# class Usuario:
      # seu código vai aqui

class Usuario():
    def __init__(self, primeiroNome=""):
        self.__primeiroNome = primeiroNome

    def setNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getNome(self):
        return f"O nome é {self.__primeiroNome}."

# Instanciação
usuario1 = Usuario()
usuario1.setNome("Joe")

print(usuario1.getNome())


