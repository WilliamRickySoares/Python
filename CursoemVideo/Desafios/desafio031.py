"""
Exercício Python 31:
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45
parta viagens mais longas.
"""

a = float(input('\nQual a distância da viagem em Km: '))
if a <= 200:
    p = a * 0.50
else:
    p = a * 0.45
print('\nO preço da passagem é de \033[35mR$ {:.2f}\033[m'.format(p))
