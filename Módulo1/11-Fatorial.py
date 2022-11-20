# Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
numero = int(input('Digite um número inteiro: '))

def fatorial(n):
    if n == 1:
         return 1
    else:
         return n * fatorial(n-1)

print(fatorial(numero))