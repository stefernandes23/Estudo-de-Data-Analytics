# Elabore um algoritmo em Python que peça 2 números inteiros e um número decimal.
# Faça uma função para calcular cada item e apresente as respostas:
# 1. O produto do dobro do primeiro com a metade do segundo.
# 2. A soma do triplo do primeiro com o terceiro.
# 3. O terceiro elevado ao cubo. funções


valor1 = int(input('Valor um: '))
valor2 = int(input('Valor dois: ' ))
valor3 = float(input('Valor três: '))

def multiplicar(valor1, valor2):
    return ((valor1*2) * (valor2/2))

def soma(valor1, valor3):
    return(valor1*3 + valor3)

def elev(valor3):
    return(valor3**3)

resultado = multiplicar(valor1,valor2)
resultado2 = soma(valor1,valor3)
resultado3 = elev(valor3)

print (f'{resultado} \n{resultado2} \n{resultado3}')




