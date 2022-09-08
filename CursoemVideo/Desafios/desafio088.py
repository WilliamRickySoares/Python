print("""
Exercício 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.
""")

from random import randint
from time import sleep
apostas = int(input(f'Qual a quantidade de apostas deseja fazer? '))
jogo = list()
lista = []

print('')
print(f'*** Sorteando números para {apostas} apostas! ***')
for a in range(0, apostas):
    # print(a)
    while len(jogo) < 6:
        n = randint(1, 60)
        if n not in jogo:
            jogo.append(n)
    jogo.sort()
    lista.append(jogo[:])
    jogo.clear()

sleep(0.5)
for e, v in enumerate(lista):
    sleep(1)
    print(f'Jogo {e + 1}: {v}')
sleep(0.5)

print(f'************* Boa sorte !! **************\n')
# Lista completa
print(lista)
