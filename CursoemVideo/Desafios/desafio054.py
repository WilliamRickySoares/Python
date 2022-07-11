"""
# Aula 013
# Desafios 054
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessas ainda não atingiram a maioridade
e quantas já são maiores.
"""
from datetime import date
ano = date.today().year - 18
# print(ano)
maior = 0
menor = 0

for i in range(0, 7):
    p = int(input('Digite o ano de nascimento da pessoa: '))
    if p > ano:
        # print('Menor')
        menor += 1
    else:
        # print('Maior')
        maior += 1

print(f'\nTotal de \033[1:32m{maior}\033[m são de maior e \033[1:33m{menor}\033[m são de menor.')
