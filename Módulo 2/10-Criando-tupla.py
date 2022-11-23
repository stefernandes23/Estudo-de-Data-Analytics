# '''
# * Crie uma tupla a partir de uma lista de nomes e exiba em tela uma mensagem de saudações para cada uma delas;
# * Tente alterar um ou mais itens das tuplas e demonstre a imutabilidade das tuplas;
# * Experimente alguns métodos aprendidos em listas aplicados a tuplas; 

lista_nomes = ['Barbara','Joanna','Laura','Daiane','Luiza']

tupla_nomes = tuple(lista_nomes)


try:
    tupla_nomes.append('Maria')
    del tupla_nomes[0]
    tupla_nomes.pop()
    tupla_nomes.remove("Lucas")
except:
    print(tupla_nomes)
    print("A tupla é imutável!!!!!!!!!\n")




lista_nomes.pop(3)
lista_nomes.append('Priscilla')
lista_nomes.remove("Luiza")

print(lista_nomes)
print('Já a lista é mutável!')

