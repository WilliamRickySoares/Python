"""
Exercício Python 28: Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint
from time import sleep
print('-*-' * 18)
print('Tente adivinhar o número de 0 a 5 que estou pensando')
print('-*-' * 18)

c = randint(0, 5)
j = int(input('\nQual foi o número que eu pensei? '))
print('PROCESSANDO...\n')
sleep(2)
if c == j:
    print('PARABÉNS! Você adivinhou o número que eu estava pensando')
else:
    print('GANHEI! Você errou, eu estava pensando no número {}'.format(c))
