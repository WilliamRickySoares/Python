'''
Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura
while.
'''

n1 = int(input('Insira o primento termo: '))
raz = int(input('Insira a razão da progressão: '))
lim = int(input('Quantos termos quer visualizar: '))
i = 1
print(f'\nOs primeiros {lim} termos da progressão aritimética com uma razão de '
      f'\033[1:33m{raz}\033[m iniciada em \033[1:33m{n1}\033[m:\n {n1},', end=' ')
while i != lim:
    n1 += raz
    if i == (lim-1):
        print(n1, end='.\n')
    else:
        print(n1, end=', ')
    i += 1
