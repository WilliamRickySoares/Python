'''
Desafio 058
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar"
em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer.
'''

from random import choice, randint
from time import sleep
think = '\nPensando em um número de 1 a 10'
dot = '.'
t = 0

# Se usar listas, usar random.choice
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# escolha = choice(lista)

# se usar inteiros, usar random.randint
escolha = randint(0, 10)
print(think, end='')
for i in range(1, 6):
    print(dot * 1, end='')
    sleep(0.4)

j = int(input('\nEscolha um número e tente acertar: '))
while escolha != j:
    print(f'\nPense em um número diferente de \033[1:31m{j}\033[m.')
    if j > escolha:
        dica = 'menor'
    else:
        dica = 'maior'
    j = int(input(f'Tente novamente, escolha um número {dica}: '))
    t += 1
else:
    print(f'\nVocê acertou depois de \033[1:31m{t}\033[m tentativas, o número que pensei era o '
          f'\033[1:32m{escolha}\033[m.')
