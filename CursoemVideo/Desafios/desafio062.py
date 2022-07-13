'''
Desafio 062
Melhore o desafio 061, perguntando para o usuário se ele quer
mostrar mais alguns termos. O programa encerra quando ele disser
que quer mostrar 0 termos.
'''

i = 1
q = 's'
while q != 'n':
    n1 = int(input('\nInsira o primento termo: '))
    raz = int(input('Insira a razão da progressão: '))
    lim = int(input('Quantos termos quer visualizar: '))
    print(f'Os primeiros {lim} termos na progressão aritimética com uma razão de '
          f'\033[1:33m{raz}\033[m, iniciada em \033[1:33m{n1}\033[m: {n1},', end=' ')
    while i != lim:
        n1 = n1 + raz
        if i == (lim-1):
            print(f'{n1}.\n')
        else:
            print(n1, end=', ')
        i += 1
    q = str(input('Quer visualizar outra PA? [S/N] ')).lower()
