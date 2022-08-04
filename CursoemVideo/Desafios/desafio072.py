print("""Desafio 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.""")

tupla = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze'
         , 'quatorze', 'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')

while True:
    num = int(input('\nDigite um número entre 1 e 20: '))
    if 1 <= num <= 20:
        print(f'Você digitou {tupla[num - 1]}.')
    else:
        print(f'Foi digitado um valor fora do intervalo solicitado. O programa será encerrado!')
        break
