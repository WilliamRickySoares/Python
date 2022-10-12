"""Desafio 091
Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados num dicionário.
No final, coloque esse dicionário em ordem, sabedo que o vencedor tirou o maior número no dado.
"""

from random import randint
from operator import itemgetter
jogadores = dict()
rank = dict()
nomes = list()
n = int(input('Quantos jogadores vão participar? '))
d = int(input('Quando lados tem o dado? '))

minimo = maximo = 1
for j in range(0, n):
    p = f'Jogador {j + 1}'
    jogadores[p] = randint(1, d)
    if jogadores[p] <= minimo:
        minimo = jogadores[p]
    elif jogadores[p] > maximo:
        maximo = jogadores[p]
        nomes.clear()
        nomes.append(p)
    elif jogadores[p] == maximo:
        maximo = jogadores[p]
        nomes.append(p)

rank = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
for i, k in enumerate(rank):
    print(f"O {i + 1}º é o {k[0]} com {k[1]} pontos.")

print('')
for k, v in jogadores.items():
    print(f'\nO {k} tirou {v} no d{d}', end = '')
    if k in nomes:
        print(' e tirou o maior número no dado', end = '')

print('')
jogadores['ganhadores'] = nomes
print(f'\n\nA dic completa : {jogadores}')
