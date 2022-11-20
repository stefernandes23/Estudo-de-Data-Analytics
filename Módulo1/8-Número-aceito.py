# Faça um programa que peça um número, entre zero e dez.
# Mostre uma mensagem ("Número aceito") em caso de valor válido. 
# Caso o valor seja inválido, informe ao usuário e continue pedindo até que um valor válido seja inserido.

numero_inicial = int(input('Digite: '))
loop = True
while loop == True:
    if numero_inicial >= 0 and numero_inicial <= 10 :
        print('Número aceito!')
        loop = False
    else:
        print ('Número inválido, tente novamente!')
        numero_inicial = int(input('Digite: '))

