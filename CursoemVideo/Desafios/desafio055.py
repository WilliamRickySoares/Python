"""
# Aula 013
# Desafio 055
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""

lista = []
lim = 5
seq = 0

for i in range(0, lim):
    a = float(input(f'Digite o peso da {i+1}º pessoa: '))
    lista.append(a)
    seq = sorted(lista)
    # print(seq)

print(f'A pessoa com menor peso tem {seq[0]:.2f}kg e a pessoa com maior peso tem {seq[lim-1]:.2f}kg.')
