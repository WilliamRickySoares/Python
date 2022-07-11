"""
# Aula 013
# Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Exemplos de palíndromo:
    "APOS A SOPA",
    "A SACADA DA CASA"
    "A TORRE DA DERROTA"
    "O LOBO AMA O BOLO"
    "ANOTARAM A DATA DA MARATONA"
"""

frase = str(input('Digite a frase: '))
phase = (frase.strip().replace(" ", ""))
m = len(phase)
t = 0

for c in range(0, m):
    i = 0 + c
    f = m - (c + 1)
    # if phase[i] == phase[f]:
    #     print(f'{phase[i]} = {phase[f]}')
    #     print('iguais')
    # else:
    #     print(f'{phase[i]} \u2260 {phase[f]}')
    #     print('dif')
    if phase[i] == phase[f]:
        t += 1

if t == m:
    print(f'\nOs caraceteres posicionados inversamente geram a mesma frase, ou seja,'
          f' é um \033[1:32mpalíndromo\033[m.')
else:
    print(f'\nA frase invertida não gera a mesma frase, ou seja, não é um \033[1:31mpalíndromo\033[m.')
