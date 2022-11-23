# * Crie um dicionário de dicionários de cidades em que as chaves são o nome da cidade e o estado a que ela pertence;
# * Armazene a população, se há praia, região em que está inserida e o gentílico da cidade;
# * Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela;

riodejaneiro = {"População": "6,748 milhões", "Praia": "Sim", "Região":"Sudeste", "Gentílico": "Carioca"}
saopaulo = {"População": "12,33 milhões", "Praia": "Sim", "Região":"Sudeste", "Gentílico": "paulistano"}
recife = {"População": "1,6 milhão", "Praia": "Sim", "Região":"Nordeste", "Gentílico": "recifense"}
belohorizonte = {"População": "2,72 milhão", "Praia": "Não", "Região":"Sudeste", "Gentílico": "Belo-horizontino"}
manaus = {"População": "2,02 milhões", "Praia": "Sim", "Região":"Norte", "Gentílico": "Manauara"}

cidades_dict = {'Rio de Janeiro': riodejaneiro,
'São Paulo': saopaulo,
'Recife': recife,
'Belo Horizonte': belohorizonte,
'Manaus': manaus
}

for cidade in cidades_dict:
    print(f"{cidade} - {cidades_dict[cidade]}")