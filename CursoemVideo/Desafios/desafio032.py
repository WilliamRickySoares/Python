"""
Exercício Python 32:
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
"""

from datetime import date

ano = int(input('Digite o ano: '))
if ano == 0:  # quando digitar 0 (zero)
    ano = date.today().year  # identificar qual o ano atual (do sistema)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano \033[33m{}\033[m é bissexto.'.format(ano))
else:
    print('O ano \033[31m{}\033[m \033[1mNÃO\033[m é um ano bissexto.'.format(ano))
