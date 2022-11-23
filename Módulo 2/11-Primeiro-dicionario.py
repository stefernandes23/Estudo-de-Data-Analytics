dicionario = {"python":'Python é uma linguagem de programação de alto nível, interpretada de script,\nimperativa, orientada a objetos, funcional, de tipagem dinâmica e forte. Foi lançada por Guido van Rossum \nem 1991' , 
"r": 'R é uma linguagem de programação multi-paradigma orientada a objetos, programação funcional, dinâmica,\nfracamente tipada, voltada à manipulação, análise e visualização de dados. Foi criado originalmente \npor Ross Ihaka e por Robert Gentleman no departamento de Estatística da Universidade de Auckland, Nova Zelândia.' , 
"análise exploratória": 'Em estatística, a análise exploratória de dados é uma abordagem à análise de conjuntos de dados\nde modo a resumir suas características principais, frequentemente com métodos visuais. ',
"pandas":'Em programação de computadores, pandas é uma biblioteca de software criada para a linguagem Python para manipulação\ne análise de dados. Em particular, oferece estruturas e operações para manipular tabelas\n numéricas e séries temporais. É software livre sob a licensa licença BSD.', 
"powerbi":'O Microsoft Power BI é um serviço de análise de negócios e analise de dados da desenvolvedora Microsoft lançado a 24\nde julho de 2015.'}

rodando = True
while rodando == True:
    pesquisar = input('Qual é a palavra? ').lower()
    if pesquisar in dicionario:
        print(f'A definição de {pesquisar} é: {dicionario[pesquisar]}')
    else:
        print('Essa palavra não está no dicionário.')
