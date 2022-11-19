'''Escreva um algoritmo que declare o salário mensal atual de um funcionário em uma variável e o percentual de reajuste em outra. 
Calcule e exiba o valor do novo salário'''
salario = float(input("Salário: "))
aumentoSalario = salario * 0.05
print(f'O salário ficará: {aumentoSalario + salario}')
print(type(salario))
print(type(aumentoSalario))