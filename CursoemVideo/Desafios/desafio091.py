"""Desafio 091
Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados num dicionário.
No final, coloque esse dicionário em ordem, sabedo que o vencedor tirou o maior número no dado.
"""

from random import randint
jogadores = {}
nomes = []
n = int(input('Quantos jogadores vão participar? '))
d = int(input('Quando lados tem o dado? '))

minimo = maximo = 1
for j in range(0, n):
    p = f'{j + 1}º Jogador'
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

for k, v in jogadores.items():
    print(f'\nO {k} tirou {v} no d{d}', end = '')
    if k in nomes:
        print(' e tirou o maior número no dado', end = '')

jogadores['ganhadores'] = nomes
print(f'\n\nA dic completa : {jogadores}')
