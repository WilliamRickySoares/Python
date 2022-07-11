"""
# Aula 013
# Desafio 052
Faça um prograam que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número: '))
r = 0

for c in range(1, n-1):
    c += 1
    r = n % c
    r += r
    if r == 0:
        print(f'\033[1:32m{n}\033[m pode ser dividido por \033[1:31m{c}\033[m, então não é um número primo')

print(f'\n\033[1:32m{n}\033[m é um numero primo')


