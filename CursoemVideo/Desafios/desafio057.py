'''
Desafio 057
Faça um programa que leia o sexo de uma pessoa,
mas só aceite os valores 'M' ou 'F'.
Caso esteja errado, peça a digitação novamente até ter um valor correto
'''

ok = True
while ok:
    s = str(input(f'\nDigite seu sexo [M/F]: ')).upper()
    if s == 'M' or s == 'F':
        print(f'Obrigado, vc escolheu a opção \033[1:32m{s}\033[m.')
        ok = False
    else:
        print(f'Voce digitou \033[1:31m{s}\033[m. Favor escolher entre '
              f'\033[1:35m[F]\033[m para feminino ou \033[1:34m[M]\033[m para masculino.')
