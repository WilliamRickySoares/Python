"""
Exercício Python 33:
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
"""

n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))

maior = n3
if n1 > n2 and n1 > n3:
    maior = n1
elif n2 > n1 and n2 > n3:
    maior = n2
print('\nO maior valor é o \033[33m{}\033[m'.format(maior))

if n1 < n2 and n1 < n3:
    menor = n1
elif n2 < n1 and n2 < n3:
    menor = n2
else:
    menor = n3
print('O menor valor é o \033[32m{}\033[m'.format(menor))

