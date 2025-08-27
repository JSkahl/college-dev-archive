import random

animals = [
    "cat",
    "bat",
    "frog",
    "wolf",
    "otter",
    "koala",
    "monkey",
    "parrot",
    "elephant",
    "panther",
    "dolphin",
    "jackal",
]

tools = [
    "axe",
    "drill",
    "saw",
    "pick",
    "hammer",
    "pliers",
    "wrench",
    "cutter",
    "toolbox",
    "leveler",
    "clampers",
    "chisel",
]

sports = [
    "golf",
    "judo",
    "yoga",
    "ski",
    "tennis",
    "boxing",
    "soccer",
    "hockey",
    "cricket",
    "cycling",
    "baseball",
    "wrestle",
]


print("=========================")
print("=== Jogo do Embaralho ===")
print("=========================")
print("")
level = int(
    input(
        "Selecione um nível: 1, 2 ou 3 (Fácil, Intermediário e Difícil, respectivamente)"
    )
)
theme = int(
    input(
        "Selecione o tema: 1, 2 ou 3 (Animais, Ferramentas e Esportes, respectivamente)"
    )
)

words = []


def get_theme():
    if theme == 1:
        return animals
    if theme == 2:
        return tools
    if theme == 3:
        return sports


def get_words(size):
    for i in get_theme():
        if len(i) <= size:
            words.append(i)


if level == 1:
    get_words(4)
if level == 2:
    get_words(6)
if level == 3:
    get_words(8)

rnd_word = random.choice(words)
word = list(rnd_word)
random.shuffle(word)

print("A palavra embaralhada é: ", "".join(word))
print("")
print("=========================")
print("")


acertou = False
c = 1

while c <= 5:
    tentativa = input("Tente: ")

    if tentativa == rnd_word:
        acertou = True
        if c == 1:
            print(f"Boa! Acertou em {c} tentativa.")
        print(f"Boa! A palavra era {rnd_word} e você acertou em {c} tentativas.")
        break
    else:
        if c == 1:
            print(f"Acerta da próxima! Só mais {5 - c} tentativas.")
        elif c == 5:
            print(f"Acerta da próxima! Você errou a palavra {rnd_word}.")
        elif c == 4:
            print(f"Acerta da próxima! Só mais {5 - c} tentativa.")
        else:
            print(f"Acerta da próxima! Só mais {5 - c} tentativas.")

    c = c + 1
