"""
# Aula 013
# Desafio 048
Faça um program que calcule a soma entre todos os números impares
que são multiplos de três e que se encontram no intervalo de 1 até 500
"""
i = int(input('Digite o numero inicial: '))
f = int(input('Digite o numero final: '))

cont = 0
t = 0

for c in range(i, f+1, 2):
    # print(c, end=' ')
    if c % 3 == 0:
        t += c
        cont += 1
        # print(f'Contagem c {c}')
        # print(f'Total {t}')
print(f'\nA soma entre todos {cont} números impares entre {i} e {f} é \033[1:32m{t}\033[m.')
