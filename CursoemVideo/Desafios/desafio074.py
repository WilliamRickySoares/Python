print("""
Desafio 074 (M3A16)
Crie um programa que vai gerar cinco números aleatorios e colocar em um tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.\n""")

#  TODO: Copiado do exemplo, não realizado previamente

from random import randint

n = (randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20), randint(1, 20))
print(f'Os números sortados foram {n}')
print(f'O maior número é {max(n)}.')
print(f'O menor numero é {min(n)}.')

