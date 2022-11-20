# Faça uma função que retorne o reverso de um número inteiro informado.
# Crie uma função que permita contar o número de vezes que aparece uma letra em uma string.

# Atividade 1
def mostrar_retorno (num):
    return str(num[::-1])

numero = (input('Digite um numero: '))
print (mostrar_retorno(numero))


# Atividade 2
def nomC(nome):
    nomes = nome.replace(' ','')
    return len(nomes)

nome = input ('Digite seu nome: ')
print (nomC(nome))
