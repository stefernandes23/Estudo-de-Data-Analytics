# - Faça uma lista de suas pizzas favoritas;
# - Faça uma cópia chamanda friend_pizzas;
# - Adicione uma nova pizza a lista original;
# - Adicione uma pizza diferente a lista friend_pizzas;
# - Prove que as duas listas são diferentes:
#     -> Exiba a mensagem "Minhas pizzas favoritas são:"; em seguida, exiba a primeira lista;
#     -> Exiba a mensagem "As pizzas favoritas do meu amigo são:"; em seguida, exiba a segunda lista;
# Certifique-se de que cada pizza nova esteja armazenada na lista apropriada; 

lista_pizzas = ['Calabresa','Portuguesa','4 Queijos','Margherita','Marshmallow']

friend_pizzas = lista_pizzas.copy()

friend_pizzas.append('Banana com canela')

print (f'As minhas pizzas favoritas são {lista_pizzas} \nJá as pizzas favoritas do meu amigo são {friend_pizzas}')