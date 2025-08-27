# Primeiro exercicio

pessoas = {
    'Jose': 19,
    'Pedro': 15,
    'Cleber': 24,
    'Julia': 27,
    'Rodrigo': 34,
    'Paulo': 32,
    'Jeremias': 65,
    'Gabriel': 73,
    'Christian': 14,
    'Bruno': 8
}


# Segundo exercicio
#
#for i in pessoas:
#    print(f"{i}, {pessoas[i]} anos.")


# Terceiro exercicio
#
#def get_age(nome):
#    # Formata o nome
#    new_nome = nome.lower().capitalize()
#
#    print(f"{new_nome} tem {pessoas[new_nome]} anos.")
#
#get_age("bruno")


# Quarto exercicio
#
#def put_age(nome, newAge):
#    new_nome = nome.lower().capitalize()
#
#    print("Informações antigas:")
#    print(f"{new_nome}, {pessoas[new_nome]} anos.")
#    print("")
#    pessoas[new_nome] = newAge
#    print("Informações novas:")
#    print(f"{new_nome}, {pessoas[new_nome]} anos.")
#
#put_age("Jose", 20)


# Quinto exercicio
#
#def delete_person(nome):
#    new_nome = nome.lower().capitalize()
#    pessoas.pop(new_nome)
#
#    print(f"Pessoa deletada: {new_nome}")
#    for i in pessoas:
#        print(i, pessoas[i])
#
#delete_person("jose")


# Sexto exercicio
#
#def count_people():
#    counter = 0
#
#    for i in pessoas:
#        counter = counter + 1
#
#    print(f"O dicionário contém {counter} pessoas.")
#
#count_people()


# Sétimo exercicio
#
#def average_age():
#    counter = 0
#    c = 0
#
#    for i in pessoas:
#        c = c + pessoas[i]
#        counter = counter + 1
#
#    media = c / counter
#
#    print(f"A média de todas as idade é de {round(media, 1)} anos")
#
#average_age()


# Oitavo exercicio
#
#def older_person():
#    older = ""
#    last = 0
#
#    for i in pessoas:
#        if pessoas[i] > last:
#            older = i
#        last = pessoas[i]
#
#    print(older)
#
#older_person()


# Nono exercicio
#
#def younger_person():
#    younger = ""
#    last = 0
#
#    for i in pessoas:
#        if pessoas[i] < last:
#            younger = i
#        last = pessoas[i]
#
#    print(younger)
#
#younger_person()


# Décimo exercicio
#
#def first_character(c):
#    for i in pessoas:
#        if i[0].lower() == c.lower():
#            print(i)
#
#first_character("p")
