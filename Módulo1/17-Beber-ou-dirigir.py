idade  = int(input('Qual sua idade? '))
def dirigirOuBeber(idade):
    if idade >= 18:
        return ("Ja pode dirigir e beber, mas por favor não faça os dois juntos")
    else:
        return  ("Não pode beber nem dirigir")


print (dirigirOuBeber(idade))