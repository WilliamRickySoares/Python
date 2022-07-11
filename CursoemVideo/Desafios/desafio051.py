"""
# Aula 013
# Desafio 050
Desevolva um programa que leia o primeiro termo e a razão de uma progressão aritimética.
No final, mostre os 10 primeiros termos dessa progração.
"""

i = int(input('Digite o primeiro termo: '))
p = int(input('Digite a razão de progressão: '))
r = 0

for c in range(1, 11):
    i += p
    print(i)


