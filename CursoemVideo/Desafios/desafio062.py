'''
Desafio 062
Melhore o desafio 061, perguntando para o usuário se ele quer
mostrar mais alguns termos.
'''

n1 = int(input('Insira o primento termo: '))
raz = int(input('Insira a razão da progressão: '))
lim = int(input('Quantos termos quer visualizar: '))
cont = 0
while lim != 0:
    i = 0
    print(f'Os primeiros {lim} termos na progressão aritimética com uma razão de '
          f'\033[33m{raz}\033[m iniciada em \033[33m{n1}\033[m:', end=' ')
    while i != lim:
        if i == (lim-1):
            print(f'\033[1:32m{n1}\033[m.\n')
        else:
            print(f'\033[1:32m{n1}\033[m', end=', ')
        n1 += raz
        i += 1
        cont += 1
    lim = int(input('Quantos termos quer visualizar a mais: '))
print(f'Total de termos solicitados: \033[1:31m{cont}\033[m')
