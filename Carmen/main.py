# POC para o jogo "Onde no Brasil está Carmen Sandiego?"
import random


# TODO Substituir os números pelo código da cidade. Ex.: Manaus [MAO]
todas_cidades = ['SAO', 'MAO', 'SPA', 'FOR', 'VIT', 'ZPT', 'XPTO', 'ZZZ', 'AAA', 'BBB']
cidades_vistas = []


def cidade_roubo():
    cidade_escolhida = str(random.sample(todas_cidades, 1))
    characters = "']["
    for i in range(len(characters)):
        cidade_escolhida = cidade_escolhida.replace(characters[i], "")
    todas_cidades.remove(cidade_escolhida)
    cidades_vistas.append(cidade_escolhida)
    print(cidade_escolhida)

# sortei cidade

def sorteia_cidade():
    cidade_escolhida = str(random.sample(todas_cidades, 1))
    characters = "']["
    for i in range(len(characters)):
        cidade_escolhida = cidade_escolhida.replace(characters[i], "")
    todas_cidades.remove(cidade_escolhida)
    cidades_vistas.append(cidade_escolhida)
    print(cidade_escolhida)


player = input('Agente no teclaro, por favor identifique-se: ')
print('Bem vindo {}'.format(player) )
continuar = input('Você foi identificado como agente da agência, deseja iniciar uma nova missão? [S/N]: ')

if continuar == 'N':
    pass

# TODO Refatorar para não precisar retirar os caraceteres especiais
# TODO Criar lista de roubos que o jogador atual já resolveu, e não permitir que ele recupere novamente
