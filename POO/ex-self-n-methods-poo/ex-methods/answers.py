# Programação Orientada a Objetos

# Esse arquivo contém as respostas das questões
# práticas da atividade sobre 'métodos mágicos' referentes
# à classe de Programação Orientada à Objetos, 
# mestrada pelo Professor Paulo César.


# Questões

# Exercício de codificação

# Vamos voltar para a classe Usuario que desenvolvemos nas
# atividades anteriores. E agora vamos definir os valores
# para o primeiro e último nome através de um método construtor.
# Esta é a classe Usuario:
#
# class Usuario():
#     primeiroNome = “”
#     ultimoNome = “”

class Usuario():
    # Método construtor
    def __init__(self, primeiroNome, ultimoNome):
        self.primeiroNome = primeiroNome
        self.ultimoNome = ultimoNome

    # Método para a busca do nome completo
    def getNomeCompleto(self):
        return f"O nome completo do usuário é: {self.primeiroNome} {self.ultimoNome}!"

usuario1 = Usuario("Bravo", "Johnny")
print(usuario1.getNomeCompleto())
