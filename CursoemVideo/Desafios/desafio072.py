print("""Desafio 072 (M3A16)
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.\n""")

tupla = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
         'seis', 'sete', 'oito', 'nove', 'dez',
         'onze', 'doze', 'treze', 'quatorze', 'quinze',
         'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('Digite um número entre 1 e 20: '))
    if 0 <= num <= 20:
        print(f'Você digitou {tupla[num]}.')
    else:
        print(f'\nVocê digitou {num}, favor digitar um número entre 1 e 20. ', end='')

    e = ' '
    while e not in 'SsNn':
        e = str(input('\nDeseja continuar? [S/N] ')).strip().upper()[0]
    if e in 'Nn':
        break

# q = ''
# while q not in 'NnSs':

