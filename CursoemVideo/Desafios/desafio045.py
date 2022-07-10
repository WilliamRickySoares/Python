"""
Desafio 045
Crie um programa que faça o computador jogar "Jokenpò" com você.

TODO: Alterar para o jogo do Sheldon - Big Bang Theory
"""

from random import choice
from time import sleep

print('\n\033[1:33m====== JOKENPÔ ======\033[m')
print('''
Escolha uma das opções
[ 1 ] Pedra \U0001f918
[ 2 ] Papel \U0001f9fb
[ 3 ] Tesoura \u2702
''')

op = [1, 2, 3]
lista = ['pedra', 'papel', 'tesoura', 'Spock', 'lagarto']
emoji = ['\U0001f918', '\U0001f9fb', '\u2702', '\U0001f596', '\U0001f98e']
lista_acao = ['esmaga', 'cobre', 'corta']
p1 = int(input('Qual a sua jogada? '))

bot = int(choice(op))
bot_nome = str(lista[bot - 1])
p1_nome = str(lista[p1 - 1])

sleep(0.5)
print('Jo')
sleep(1)
print('Ken')
sleep(1)
print('Po!!!')

if p1 == 1 and bot == 2 or p1 == 2 and bot == 3 or p1 == 3 and bot == 1:
    print('{} {} {} {} {}, você \033[1:31mPERDEU\033[m!'
          .format(bot_nome.title(), emoji[bot-1], str(lista_acao[bot - 1]), p1_nome, emoji[p1-1]))

elif p1 == 1 and bot == 3 or p1 == 3 and bot == 2 or p1 == 2 and bot == 1:
    print('{} {} {} {} {}, você \033[1:32mGANHOU\033[m!'
          .format(p1_nome.title(), emoji[p1-1], str(lista_acao[p1 - 1]), bot_nome, emoji[bot-1]))
elif p1 == bot:
    print('Ambos jogaram {} {}, é um \033[1:33mEMPATE\033[m!'.format(p1_nome, emoji[p1-1]))
else:
    print('Escolha uma das opções entre 1, 2 ou 3')
