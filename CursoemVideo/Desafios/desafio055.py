"""
# Aula 013
# Desafio 055
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

# a = float(input('Digite o peso da pessoa: '))
# b = float(input('Digite o peso da pessoa: '))
# c = float(input('Digite o peso da pessoa: '))
# d = float(input('Digite o peso da pessoa: '))
# e = float(input('Digite o peso da pessoa: '))
#
# lista = sorted([a, b, c, d, e])
# print(f'A pessoa com menor peso tem {lista[0]:.2f} e a pessoa com maior peso tem {lista[4]:.2f}')
lista = []
lim = 5
seq = 0

for i in range(0, lim):
    a = float(input('Digite o peso da pessoa: '))
    lista.append(a)
    seq = sorted(lista)
    # print(seq)

print(f'A pessoa com menor peso tem {seq[0]:.2f} e a pessoa com maior peso tem {seq[lim-1]:.2f}')
