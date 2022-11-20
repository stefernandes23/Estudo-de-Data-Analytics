# Crie um algoritmo que deve:
# * Receber um número positivo.
# * Retornar uma sequencia de números, em ordem crescente, na qual exiba em tela
# apenas os números múltiplos de 3 até aquele número.

numero_positivo = int(input("Digite um número: "))

for c in range(0,numero_positivo+1,1):
    if c % 3 == 0:
        print(c)

print('FIM')