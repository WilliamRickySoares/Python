'''
Desafio 063
Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex.:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

ini = int(input('\nEscolha o número inicial: '))
ele = int(input('Quantos termos deseja visualizar: '))
ult = ini + ele
# print(f'\nult = {ult}\n')
# f = 1
f1 = 1
f2 = 0
lista = [0, 1]
# print(lista)

print(f'Fibonacci: ', end='')
i = 1
while i != ult:
    f = f1 + f2
    f2 = f1
    f1 = f
    # print(f'{f}', end=' ')
    lista.append(f)
    i += 1
print(f'{lista.index(ini)}')

# fonte: 'https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci' em 13/07/2022 as 12:25
