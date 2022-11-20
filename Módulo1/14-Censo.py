# Foi feita uma pesquisa entre os habitantes de uma região. Foram coletados os dados de idade, sexo e salário.
# Faça um algoritmo que leia esses dados coletados e informe:
# a) A média de salário do grupo;
# b) Maior e menor idade do grupo; 
# c) Quantidade de homens e mulheres;
# d) Quantidade de mulheres com salário até 1000;
 
# * Encerre a entrada de dados quando for digitada uma idade negativa

maior_idade = 1
menor_idade = 100000
salario_media = 0 
salario_valor = 0
mulheres_quantidade = 0
salario = 0
idade = 0
false = True
mulheres_salario_inferior = 0
homens = 0

while false == True: 
    idade = int(input('Qual a sua idade? '))
    if idade <= 0:
        break
    if idade > maior_idade:
        maior_idade = idade 
    if idade < menor_idade:
        menor_idade = idade
    
    salario = int(input('Qual seu salário? '))
    if salario > 0:
        salario_media = salario_media + 1
        salario_valor = salario_valor + salario
   
    sexo = str(input('Qual seu sexo? '))
    if sexo == 'F' or sexo == 'f':
        mulheres_quantidade = mulheres_quantidade + 1
    elif sexo == 'm' or sexo == 'M':
        homens += 1
    if  salario <= 1000 and sexo == 'F' or sexo == 'f':
        mulheres_salario_inferior+=1

   

print (f'Quantidade de mulheres: {mulheres_quantidade}')
print (f'Quantidade de homens: {homens}')
print (f'Média salarial: {salario_valor//salario_media}')
print (f'Maior idade: {maior_idade}')
print (f'Menor idade: {menor_idade}')
print(f'{mulheres_salario_inferior} mulheres recebem salário inferior ou igual a 1000')





   

