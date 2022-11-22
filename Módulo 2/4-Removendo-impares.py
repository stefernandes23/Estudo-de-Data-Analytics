'''
Elabore um algoritmo que leia uma lista de quinze números, remova os 
elementos ímpares, ordene e exiba em tela o menor e o maior valor
'''

lista_1 = [1,2,3,4,5,6,7,8,9,10,11,12]

for num in lista_1:
    if num % 2 == 1:
        lista_1.remove(num)


print(lista_1)