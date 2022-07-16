'''
Desafio 062
Melhore o desafio 061, perguntando para o usuário se ele quer
mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
'''

n1 = int(input('Insira o primento termo: '))
raz = int(input('Insira a razão da progressão: '))
lim = int(input('Quantos termos quer visualizar: '))
i = 1

while lim != 0:
    while i <= lim:
        print(n1, end=' -> ')
        n1 += raz
        i += 1
    print('Pause')
    lim = int(input('Quantos termos quer visualizar a mais: '))
    i = 1
