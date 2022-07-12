"""
# Aula 13
# Desafio 049
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""

r = 0
cont = 0

for c in range(0, 6):
    n = int(input('Digite um número: '))
    if (n % 2) == 0:
        r += n
        cont += 1

print(f'Total da soma dos {cont} números pares é \033[1:32m{r}\033[m.')
