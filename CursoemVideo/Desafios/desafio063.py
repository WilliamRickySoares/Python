'''
Desafio 063
Escreva um programa que leia um número N inteiro qualquer e mostre
na tela os N primeiros elementos de uma Sequência de Fibonacci.

Ex.:
0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
'''

q = int(input('Quantos termos deseja visualizar: '))
i = f = v1 = 0
v2 = 1

print(f'Os {q} primeiros termos da Sequencia Fibonacci: ', end='')

while i <= q-1:
    if i == 0:
        f = v1
    elif i == 1:
        f = v2
    else:
        f = v1 + v2
        v1 = v2
        v2 = f
    i += 1
    print(f'{f}', '\n' if i >= q else '-> ', end='')

# https://www.programiz.com/python-programming/examples/fibonacci-sequence
# nth = n1 + n2
# n1 = n2
# n2 = nth

# fonte: 'https://pt.wikipedia.org/wiki/Sequ%C3%AAncia_de_Fibonacci' em 13/07/2022 as 12:25
