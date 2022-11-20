# * Escrever um algoritmo que lê as 3 notas obtidas por um aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação.
# Calcular a média de aproveitamento, usando a fórmula:
# * MA = (Nota1 + Nota2 x 2 + nota3 x 3 + ME)/7 
# Atribuição de conceitos:
# > 9       - A
# 7,5 e < 9 - B
# 6 e < 7,5 - C
# 4 e < 6   - D
# < 4       - E 
# Ao fim informar:
# * O conceito do aluno
# * Se ele foi aprovado (A, B, C ) ou reprovado (D e E)

nome = str(input('Digite seu nome:'))
nota1 = float(input('Qual a primeira nota? '))
nota2 = float(input('Qual a segunda nota? '))
nota3 = float(input('Qual a terceira nota? '))
me = float(input('Qual a média dos exercicíos? '))

## Cálculo 
ma = (nota1 + nota2 * 2 + nota3 * 3 + me)/7

def calculo (a,b,c,d):
    return ma
resultado = calculo(nota1,nota2,nota3,me)

## Conceitos 
if resultado >= 9.0 :
    print (f' \nParabéns, {nome}!\nVocê tirou {resultado}. Seu conceito é A, você está aprovado(a)!\n')
elif resultado == 7.5 and resultado < 9.0 :
    print (f' \nParabéns, {nome}!\nVocê tirou {resultado}. Seu conceito é B, você está aprovado(a)!\n')
elif resultado == 6.0 and resultado < 7.5 :
    print (f' \nParabéns, {nome}!\nVocê tirou {resultado} Seu conceito é C, você está aprovado(a)! \n')
elif resultado == 4.0 and resultado < 6.0 :
    print (f' \nSinto muito, {nome}.\nVocê tirou {resultado}. Você está reprovado(a) pois tirou conceito D.\nMas não fique triste, continue estudando que na próxima você consegue.\n')
elif resultado < 4.0 :
    print (f' \nSinto muito, {nome}.\nVocê tirou {resultado}. Você está reprovado(a) pois tirou conceito E.\nMas não fique triste, continue estudando que na próxima você consegue.\n')

