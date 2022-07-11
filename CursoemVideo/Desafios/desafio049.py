"""
# Aula 013
# Desafio 049
Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando o laço for
"""

n = int(input('Escolha uma tabuada: '))
k = int(input('Calcular até o número: '))

print(f'\nTabuada de \033[1:32m{n}\033[m')
for c in range(1, k+1):
    t = n * c
    print(f'{c} * {n} = {t}')
