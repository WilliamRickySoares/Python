"""
# Aula 013
# Desafio 052
Faça um prograam que leia um número inteiro e diga se ele é ou não um número primo.
"""

n = int(input('Digite um número para verificar se é primo: '))
r = 0
t = 0
div = []

for c in range(2, n-1):
    r = n % c
    if r == 0:
        div.append(c)
        t += 1
if t == 0:
    print(f'O número \033[1:32m{n}\033[m é um numero primo.')
else:
    print(f'O número \033[1:32m{n}\033[m pode ser dividido por \033[1:33m{div}\033[m, então '
          f'\033[1:31mNÃO\033[m é um número primo.')
