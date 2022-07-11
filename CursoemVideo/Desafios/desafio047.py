"""
# Aula 013
# Desafio 047
Crie um programa que mostre todos os numeros pares que estão entre o intervalo de 1 e 50
"""

t = 0
for c in range(1, 50, 2):
    print(c+1, end=' ')
    t += 1

print(f'\n\nTotal de {t} números entre 1 e 50')
