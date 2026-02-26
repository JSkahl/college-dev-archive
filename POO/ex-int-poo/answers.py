# Programação Orientada a Objetos

# Esse arquivo contém as respostas das questões
# prática da atividade introdutória à classe
# de Programação Orientada à Objetos, mestrada
# pelo Professor Paulo César.

# O arquivo '.md', neste mesmo diretório,
# possuí as respostas para a parte, de fato,
# prática da atividade.


# Questões

# Exercício de codificação

# Quase todos os aplicativos ou blogs lidam com os 
# usuários. Seja o processo de registro (cadastro),
# o login e logout, o envio de lembretes aos usuários
# que perderam suas senhas ou a alteração delas sob
# demanda, todo o código que lida com os usuários pode
# ser agrupado em uma única classe. Em nosso exemplo, 
# chamamos a classe que lida com usuários, Usuario, de
# acordo com a convenção de nomenclatura vigente. Vamos
# escrever uma classe Usuario com as ferramentas que
# acabamos de adquirir. Esta classe conterá o nome
# e sobrenome de cada usuário e será capaz de dizer
# “Olá” a qualquer pessoa que use nosso aplicativo.



class Usuario: # Criação da classe

    # Criação das propriedades
    nome = ""
    sobrenome = ""

    # Criação do método de saudação
    def saudacao(self):
        print("Olá, " + self.nome + " " + self.sobrenome + "! Boas vindas!")

# Primeira instanciação da classe
usuario1 = Usuario()

# Definição dos atributos
usuario1.nome = "Paulo"
usuario1.sobrenome = "César"

# Exibição dos nomes do 'usuario1' individualmente
print("Nome do usuário: " + usuario1.nome + " " + usuario1.sobrenome)

# Utilização do método 'saudacao()' com base no objeto 'usuario1'
usuario1.saudacao()


print("\n")


# Segunda instanciação da classe
usuario2 = Usuario()

# Definição dos atributos
usuario2.nome = "Jane"
usuario2.sobrenome = "Silva"

# Exibição dos nomes do 'usuario2' individualmente
print("Nome do usuário: " + usuario2.nome + " " + usuario2.sobrenome)

# Utilização do método 'saudacao()' com base no objeto 'usuario2'
usuario2.saudacao()
