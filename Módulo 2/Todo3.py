import os


candidatos =[[5,10,8,8],[10,7,7,8], [8,5,4,9],[2,2,2,1],[10,10,8,9]]


aprovados =  []
reprovados = []
notacand =[]


os.system('cls')
rodando = True
while rodando == True:


    ola = str(input('Você deseja adicionar mais algum candidato?\nDigite [s] para sim e [x] para não: \n'''))
    if ola == 's' or ola == 'S':
        print('Ok, vamos lá: ')
        notacand.append (int(input('Qual a nota do candidato na etapa de entrevista? ')))
        notacand.append (int(input('Qual a nota do candidato na etapa do teste teórico? ')))
        notacand.append (int(input('Qual a nota do candidato na etapa do teste prático? ')))
        notacand.append (int(input('Qual a nota do candidato na etapa de avaliação de soft skils? ')))
        candidatos.append(notacand[:])   
        notacand.clear()  
    else:
        rodando = False


notae= (int(input('Qual a nota mínima na etapa de etapa de entrevista ? ')))
notat = (int(input('Qual a nota mínima na etapa do teste teórico? ')))
notap= (int(input('Qual a nota mínima na etapa do teste prático? ')))
notas= (int(input('Qual a nota mínima na etapa de avaliação de soft skills?  ')))
print()


os.system('cls')


for i in range(0,len(candidatos)):
    if candidatos[i][0] >= notae and candidatos[i][1] >= notat and candidatos[i][2] >= notap and candidatos[i][3] >= notas:
        aprovados.append(candidatos[i])
        print(f'O candidato {i+1} é compátivel com a vaga, seus resultados foram: \33[1me{candidatos[i][0]}_t{candidatos[i][1]}_p{candidatos[i][2]}_s{candidatos[i][3]}\33[0m')
    else:
        reprovados.append(candidatos[i])
        

## Se quiser ver as notas dos reprovados: 

# for i in range(0, len(reprovados)):
#     if reprovados:
#         print()
#         print (f'O candidato {i+1} não é compátivel com a vaga, seus resultados foram: \33[1me{candidatos[i][0]}_t{candidatos[i][1]}_p{candidatos[i][2]}_s{candidatos[i][3]}\33[0m')
