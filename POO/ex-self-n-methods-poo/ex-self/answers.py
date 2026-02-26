# Programação Orientada a Objetos

# Esse arquivo contém as respostas das questões
# prática da atividade sobre 'self' referentes
# à classe de Programação Orientada à Objetos, 
# mestrada pelo Professor Paulo César.

# O arquivo '.md', neste mesmo diretório,
# possuí as respostas para a parte, de fato,
# prática da atividade.


# Questões

# Exercício de codificação

# Na atividade prática anterior, escrevemos
# o método hello() dentro da classe Usuario.
# No exercício a seguir, adicionaremos a este
# método a capacidade de acessar as propriedades
# da classe com a palavra-chave self.
# A classe Usuario poderia ser codificada assim:
#
#class Usuario():
#    # as propriedades
#    primeiroNome = “”
#    ultimoNome = “”
#
#    # metodo que diz Olá ao usuario
#    def hello(self)
#        return "Olá"

class Usuario():
    # Declaração das propriedades
    primeiroNome = ""
    ultimoNome = ""

    # Método de saudação
    def saudacao(self):
        return f"Olá, {self.primeiroNome}!" 

# Instanciando classe 'Usuario'
usuario1 = Usuario()

# Declarando atributos
usuario1.primeiroNome = "Jonnie"
usuario1.ultimoNome = "Bravo"

# Utilizando método 'saudacao'
print(usuario1.saudacao())
