# Crie uma função que:
# 1- Peça a porcentagem do imposto
# 2- Subtraia a porcentagem do salário total

def calcular_imposto(valor):
   imposto = float(input('Qual a porcentagem do imposto? ')) 
   total = valor - (valor*(imposto/100))
   print(f'O salário descontado ficará de {total}')


while True:
   salario = float(input('Qual valor do salário? '))
   if salario <= 0:
      break
   else:
      calcular_imposto(salario)



