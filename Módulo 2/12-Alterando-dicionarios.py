# 
# * Altere os valores do dicionário usando os métodos de alteração;
# * Exclua três valores usando os comandos del, pop, popitem;
# * Esvazie todo o dicionário e exiba em tela o resultado final;


dicionario = {"python":'Python é uma linguagem de programação de alto nível, interpretada de script,\nimperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum \nem 1991' , 
"r": 'R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica,\nfracamente tipada, voltada à manipulação, análise e visualização de dados. Foi criado originalmente \npor Ross Ihaka e por Robert Gentleman no departamento de Estatística da Universidade de Auckland, Nova Zelândia.' , 
"análise exploratória": 'Em estatística, a análise exploratória de dados é uma abordagem à análise de conjuntos de dados\nde modo a resumir suas características principais, frequentemente com métodos visuais. ',
"pandas":'Em programação de computadores, pandas é uma biblioteca de software criada para a linguagem Python para manipulação\ne análise de dados. Em particular, oferece estruturas e operações para manipular tabelas\n numéricas e séries temporais. É software livre sob a licensa licença BSD.', 
"powerbi":'O Microsoft Power BI é um serviço de análise de negócios e analise de dados da desenvolvedora Microsoft lançado a 24\nde julho de 2015.'}


dicionario.update(r = '(ALTERADO) R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica,\nfracamente tipada, voltada à manipulação, análise e visualização de dados.')


print(f'Aqui está o valor alterado: {dicionario["r"]}\n')

dicionario.popitem()
del dicionario['python']
dicionario.pop('pandas')


dicionario.clear()
print('Dicionario vazio: ')
print(dicionario)