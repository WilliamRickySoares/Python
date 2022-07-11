"""
# Aula 013
# Desafio 048
Faça um program que calcule a soma entre todos os números impares
que são multiplos de três e que se encontram no intervalo de 1 até 500
"""

t = 0
for c in range(1, 500):
    if (c % 3) == 0:
        t += c
        # print(f'Contagem c {c}')
        # print(f'Total {t}')

print(f'A soma entre todos os números impares entre 1 e 500 é \033[1:32m{t}\033[m.')
