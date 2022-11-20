# Crie um algoritmo que deve:
# * Receber um número positivo
# * Exiba em tela uma sequência de números, em ordem decrescente, que vai daquele número até zero
# 
númeroInicial = int(input('Digite: '))

while númeroInicial >= 0 :
    print('Descendo...' + str(númeroInicial))
    númeroInicial = (númeroInicial - 1)

print ('CHEGAMOS!')