"""
Exercício Python 30:
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
"""

n = int(input('Digite um número: '))
if (n % 2) == 0:
    print('\nO número \033[34m{}\033[m é par.'.format(n))
else:
    print('\nO número \033[35m{}\033[m é impar.'.format(n))
