"""
Exercício Python 28: Escreva um programa que faça o computador “pensar”
em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir
qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import choice

lista = ['0', '1', '2', '3', '4', '5']
a = choice(lista)
e = input('Escolha um número do 0 a 5: ')
if e == a:
    print('Parabéns você acertou o número!')
else:
    print('Você erro o número. Era o número {}'.format(a))
