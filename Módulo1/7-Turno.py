# Faça um Programa que pergunte em que turno você estuda. Peça para digitar:
# * M (matutino) ou
# * V (Vespertino) ou
# * N (Noturno)
# Imprima a mensagem "Bom Dia!", "Boa Tarde!", ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

print('Em qual turno você estuda? Digite M para Matutino, V para vespertino ou N para noturno:')
turno = str(input('Digite o turno: '))

if turno == 'M' or turno == 'm':
    print('Bom dia!')
elif turno == 'V' or turno == 'v':
    print('Boa tarde!')
elif turno == 'N' or turno == 'n':
    print('Boa noite!')
else:
    print('Turno inválido! Reinicie o programa e digite a opção válida correspondente com o seu turno.')

