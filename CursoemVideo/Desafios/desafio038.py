"""
Desafio 038
Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:

- O primeiro valor é MAIOR
- O segundo valor é MAIOR
- Não existe valor maior, os dois são IGUAIS
"""

n1 = int(input('\nDigite o primeiro valor inteiro: '))
n2 = int(input('Digite o segundo valor inteiro: '))

if n1 < n2:
    print('\nO \033[1:31msegundo\033[m valor {} é maior que {}'.format(n2, n1))
elif n1 > n2:
    print('\nO \033[1:31mprimeiro\033[m valor {} é o maior que {}'.format(n1, n2))
else:
    print('\nAmbos os valores {} \033[1:32msão iguais\033[m'.format(n1))

