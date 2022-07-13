'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Exemplo:
5! = 5x4x3x2x1 = 120
'''

n = int(input('Escolha um número para fatorar: '))
r = 1
# print(f'A fatoração de {n}! é: ', end='')
for c in range(n, 0, -1):
    # print(c, end='')
    # if c != 1:
        # print(f' x ', end='')
    # else:
        # print(f' = \033[1:33m{f}\033[1:33m\n', end='')
    print(f'\nC {c}')
    if c == n:
        1