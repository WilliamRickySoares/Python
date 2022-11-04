# POC para o jogo 'Onde no Brasil está Carmen Sandiego?'
# import sys
import random

inicio = 'Segunda-feira 07:00'

# sortei cidade
todos_estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB',
                 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
trilha = [
    {'Cidade_Correta': True, 'Cidade': '', 'Estado': '',
     'Local1': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local2': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local3': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''}},
    {'Cidade_Correta': False, 'Cidade': '', 'Estado': '',
     'Local1': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local2': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local3': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''}},
    {'Cidade_Correta': False, 'Cidade': '', 'Estado': '',
     'Local1': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local2': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''},
     'Local3': {'Nome_Local': '', 'Nome_Pessoa': '', 'Fala': ''}}
]


def sorteia_cidade():
    trilha_ladrao = []
    for a in range(0, 5):
        cidade_sorteada = str(random.sample(todos_estados, 1))
        todos_estados.remove(cidade_sorteada[2:4])
        trilha_ladrao.append(cidade_sorteada[2:4])
    print(trilha_ladrao)
    print(todos_estados)


sorteia_cidade()

'''
player = input('Agente no teclaro, por favor identifique-se: ')
print(f'Bem vindo {}. '.format(player), end='')
continuar = input('Você foi identificado como agente da agência, deseja iniciar uma nova missão? [S/N]: ')

if continuar == 'N':
    sys.exit()

print('Um tesouro foi roubado de  item foi identificado como {}, sua missão é recupera-lo.'.format(sorteia_cidade()))
'''

# TODO Substituir os números pelo código da cidade. Ex.: Manaus [MAO]
# TODO Inserir o retorno da cidade dentro da str
# TODO Refatorar para não precisar retirar os caraceteres especiais
# TODO Criar lista de roubos que o jogador atual já resolveu, e não permitir que ele recupere novamente
