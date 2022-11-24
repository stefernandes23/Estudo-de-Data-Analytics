--- Selecionar todos os clientes da pizzaria. 

select * from tb_cliente;

--- Selecionar todas as pizzas.

select * from tb_pizza;

--- Selecionar todas as pizzas da categoria zero lactose.

select * from tb_pizza where tb_pizza.categoria like 'Zero Lactose'

--- Selecionar todas as pizzas que não são zero lactose.

select * from tb_pizza where tb_pizza.categoria <> 'Zero Lactose'

--- Selecionar todos os pedidos feitos no dia 21/04/2021

select id_pedido, tipo_entrega, data_pedido from tb_pedido 
where data_pedido 
between '2021-04-21 00:00:00.000' and '2021-04-21 23:59:59.999'

--- Selecionar todos os clientes que fizeram pedidos acima de 100 reais

select tb_cliente.nome, tb_pedido.id_cliente, tb_pedido.preco
from tb_cliente
join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente
where tb_pedido.preco > 100

--- Selecionar todos os sabores de pizza pedidas por enzo gabriel no dia 22-04-2021

select tb_cliente.nome, tb_pizza.nome, tb_pedido.data_pedido
from tb_pedido
join tb_cliente on tb_pedido.id_cliente = tb_cliente.id_cliente
join tb_pedido_pizza on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
where tb_cliente.nome like 'Enzo Gabriel'
and tb_pedido.data_pedido 
between '2021-04-22 00:00:00.000' and '2021-04-22 23:59:59.999'

--- Selecionar pedido de clientes que moram na Rua das Flores

select * from tb_cliente 
where tb_cliente.endereco like 'rua das _lores%' 

--- Selecionar clientes que tenham maria no emal

select * from tb_cliente
where tb_cliente.email like '%maria%'

--- Selecionar pizzas que possuem bacon

select * from tb_pizza
where tb_pizza.descricao like '%bacon%'

--- Selecionar as pizzas que possuem a letra 'a' como segundo caractere

select * from tb_pizza
where tb_pizza.nome ilike '_a%'

--- Selecionar pedidos de valores 45, 90 e 120 

select * from tb_pedido
where tb_pedido.preco = 45
or tb_pedido.preco = 90 
or tb_pedido.preco = 120

--- Retornar a soma dos valores dos pedidos 
select sum(preco) from tb_pedido

--- Retornar o pedido mais caro
select max(preco) from tb_pedido

--- Selecionar a media
select avg(preco) from tb_pedido

--- Selecionar o preço medio por categoria

select avg(tb_pedido.preco), 
tb_pizza.categoria
from tb_pedido
join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
group by tb_pizza.categoria


--- Selecionar o total dos pedidos agrupando por tipo de entrega

select sum(tb_pedido.preco)m, tipo_entrega
from tb_pedido
group by tipo_entrega

/* Selecionar o numero de pedidos que cada cliente realizou  
e ordenar de forma crescente */

select count(tb_pedido.id_cliente), tb_cliente.nome
from tb_pedido
join tb_cliente on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_pedido.id_cliente, tb_cliente.nome
order by count(tb_pedido.id_cliente) ASC

--- Selecionar o nome dos clientes que fizeram mais de dois pedidos

select tb_cliente.nome, count(tb_pedido.id_pedido)
from tb_cliente
join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente
group by tb_cliente.nome having count(tb_pedido.id_pedido) > 2;

--- Quantidade de pedidos de cada pizza
select tb_pizza.nome,tb_pizza.id_pizza, count(tb_pedido_pizza.id_pizza)
from tb_pizza
join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
group by tb_pedido_pizza.id_pizza, tb_pizza.nome,tb_pizza.id_pizza
order by count(tb_pedido_pizza.id_pizza)

--- Quantidade de pedidos de cada categoria;
select  tb_pizza.categoria, count(tb_pizza.categoria) 
from tb_pizza
group by tb_pizza.categoria;


--- Soma dos pedidos agrupados por nome;
select tb_pizza.nome, sum(tb_pedido.preco)
from tb_pizza
join tb_pedido_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
join tb_pedido on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
group by tb_pizza.nome;


--- Soma dos pedidos agrupados por categoria;
select tb_pizza.nome, sum(tb_pedido.preco), tb_pizza.categoria
from tb_pedido 
join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
join tb_pizza on tb_pizza.id_pizza = tb_pedido_pizza.id_pizza
where tb_pizza.categoria ilike 'zero lactose'
group by tb_pizza.nome, tb_pizza.categoria

--- Clientes e seus pedidos
select tb_cliente.nome , tb_pedido.id_pedido
from tb_cliente
join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente

--- Numero de pedidos feitos por cada cliente
select count(tb_pedido.id_pedido), tb_pedido.id_cliente ,
tb_cliente.nome
from tb_cliente
join tb_pedido on tb_pedido.id_cliente = tb_cliente.id_cliente
group by tb_cliente.nome, tb_pedido.id_cliente

--- Apresentar o numero de vezes que uma pizza foi pedida

select count(tb_pizza.id_pizza), tb_pizza.nome, tb_pizza.id_pizza
from tb_pizza
join tb_pedido_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
group by tb_pizza.id_pizza, tb_pizza.nome, tb_pizza.id_pizza

--- Pizza favorita cliente 1 (francisco jose!!!)

create view jose as 
select tb_pedido.id_cliente, tb_cliente.nome, 
tb_pizza.nome as "nome pizza",
tb_pizza.id_pizza
from tb_pedido
join tb_cliente on tb_cliente.id_cliente = tb_pedido.id_cliente
join tb_pedido_pizza tpp on tpp.id_pedido = tb_pedido.id_pedido
join tb_pizza on tpp.id_pizza = tb_pizza.id_pizza

select max(contando), "nome pizza"
from
(select count(id_pizza) as contando, id_pizza, jose."nome pizza"
from jose where id_cliente  = 1
group by id_pizza, jose."nome pizza") as puts
group by "nome pizza" 
order by max(contando) desc limit 1

insert into tb_pedido values (88, 1, null, 'Delivery', 50, '2021-04-21 19:41:00')
insert into tb_pedido_pizza values (88, 4, 'Inteira')

--- Pizzas menos pedidas

select min(contando), "nome pizza"
from
(select count(id_pizza) as contando, id_pizza, jose."nome pizza"
from jose
group by id_pizza, jose."nome pizza") as puts
group by "nome pizza" 
order by max(contando) asc limit 2

--- Agrupar total por endereço

select tb_cliente.endereco, sum(tb_pedido.preco)
from tb_cliente 
join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.endereco

---  Quantidade de pizzas por pedido

select count(tb_pedido.id_pedido),tb_pedido.id_pedido, tb_cliente.id_cliente, tb_cliente.nome
from  tb_pedido
join tb_pedido_pizza on tb_pedido_pizza.id_pedido = tb_pedido.id_pedido
join tb_cliente on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_pedido.id_pedido, tb_cliente.id_cliente
order by  tb_cliente.id_cliente asc

--- Apresentar os clientes e a soma de todos os seus pedidos

select tb_cliente.nome, sum(tb_pedido.preco)
from tb_cliente
join tb_pedido on tb_cliente.id_cliente = tb_pedido.id_cliente
group by tb_cliente.nome

---  Ultimo pedido de cada pizza

create view ultimo_pedido as
select max(datinha), idzinho, nomezinho, categorinha, precinho
from (select    tb_pedido.data_pedido    as datinha,
          tb_pedido_pizza.id_pizza as idzinho,
                     tb_pizza.nome as nomezinho,
                tb_pizza.categoria as categorinha, 
                   tb_pizza.preco as precinho
from tb_pedido
right join tb_pedido_pizza on tb_pedido.id_pedido = tb_pedido_pizza.id_pedido
right join tb_pizza on tb_pedido_pizza.id_pizza = tb_pizza.id_pizza
order by idzinho, datinha asc
) as joins
group by idzinho, nomezinho, categorinha, precinho
order by idzinho


select * from ultimo_pedido


