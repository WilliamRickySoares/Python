"""
# Aula 013
# Desafio 050
Desevolva um programa que leia o primeiro termo e a razão de uma progressão aritimética.
No final, mostre os 10 primeiros termos dessa progração.
"""

i = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão de progressão: '))
i2 = i
p2 = p
r = 0

print('\nProgressao Aritimética 1:', end=' ')
for c in range(1, 11):
    print(i, end=' ')
    i += p

print('\n\nProgressão Aritimética 2:', end=' ')
for c2 in range(i2, ((i2 + (10-1) * p2) + p2), p2):
    print(f'{c2}', end=' ')
