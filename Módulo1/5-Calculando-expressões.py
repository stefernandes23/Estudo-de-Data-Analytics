# Elabore um algoritmo em Python que execute os passos abaixo:
# 1. Receba 4 números (a, b, c, d)
# 2. Calcule a expressão (a*c - b*d)
# 3. Calcule a expressão (a + b + c + d)/4
# 4. Exiba os resultados na tela

valorA = int(input('Digite um valor:'))
valorB = int(input('Digite um valor:'))
valorC = int(input('Digite um valor:'))
valorD = int(input('Digite um valor:'))

calculo1 = (valorA*valorC - valorB*valorD)
calculo2 = ((valorA + valorB + valorC + valorD)/4)

print(calculo1)
print(calculo2)