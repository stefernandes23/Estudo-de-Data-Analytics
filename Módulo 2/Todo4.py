pc_analista = ['Python', 'Power Bi', 'Sql', 'Boa comunicaçãoo']
pc_cientista =['Python', 'Banco de dados', 'Machine Learning', 'Resolução De Problemas', 'Estatística']
analistas = {}
cientistas = {}
aprov_analista = []
aprov_cientista = []

inscritos_analista = 0
inscritos_cientista = 0


def vaga():
    vaga_cand = int(input('Para qual vaga o candidato está aplicando\n[1] Analista de Dados [2] Cientista de Dados: '))
    if vaga_cand == 1:
        return 'Analista de Dados'
    elif vaga_cand == 2:
        return 'Cientista de Dados'
    else:
        print('Digite uma opção válida: ')
        if vaga() == 'Analista de Dados':
            return 'Analista de Dados'
        elif vaga() == 'Cientista de Dados':
            return 'Cientista de Dados'


def analise_cv(pc_analista,cv_cand,pc_cientista):
    if escolha_vaga == 'Analista de Dados':
        for palavra in pc_analista:
            if palavra in cv_cand:
                analistas.update({'nome': nome_cand ,'vaga': escolha_vaga, 'cv': cv_cand})
                if analistas not in aprov_analista:
                    aprov_analista.append(analistas.copy())
    
    if escolha_vaga == 'Cientista de Dados':
        for palavra in pc_cientista:
            if palavra in cv_cand:
             
             
                cientistas.update({'nome': nome_cand ,'vaga': escolha_vaga, 'cv': cv_cand})
                if cientistas not in aprov_cientista:
                    aprov_cientista.append(cientistas.copy())
                

    

#Quantos candidatos serão cadastrados?
qntd_candidatos = int(input('Quantos candidatos serão cadastrados? '))

for i in range(0,qntd_candidatos, 1):
    nome_cand = str(input('Digite o nome do candidato: '))
    escolha_vaga = vaga()
    if escolha_vaga == 'Analista de Dados':
        inscritos_analista += 1
    if escolha_vaga == 'Cientista de Dados':
        inscritos_cientista += 1
    cv_cand = str(input('Informe o resumo do currículo: ')).title()
    analise_cv(pc_analista,cv_cand,pc_cientista)

count_aprov_analista = len(aprov_analista)
count_aprov_cientista = len(aprov_cientista)


print(len(analistas))
print(len(cientistas))  
# print(f'O total de candidatos para a vaga de Analista de dados {inscritos_analista} e porém apenas {count_aprov_analista} pessoas tem o resumo com as palavras que estamos buscando.')
# print(f'O total de candidatos para a vaga de Cientista de dados {inscritos_analista} e porém apenas {count_aprov_cientista} pessoas tem o resumo com as palavras que estamos buscando.')