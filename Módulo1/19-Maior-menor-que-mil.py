# Criar uma função que retorne se o número é maior, igual ou menor que mil
def maior_mil(valor):
    if valor > 1000:
        return print ('É maior que mil')
    elif valor == 1000:
        return print ('É mil')
    else:
        return print ('É menor que mil ')
        
valor = int(input('Digite um numero inteiro: '))
maior_mil(valor)