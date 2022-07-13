'''
Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos numeros
[5] Sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
'''

termo1 = int(input('Escolha o primeiro termo: '))
termo2 = int(input('Escolha um segundo termo: '))
opcao = ''

while opcao != 5:
    opcao = int(input(
    '''
        [1] Somar
        [2] Multiplicar
        [3] Maior
        [4] Novos numeros
        [5] Sair do programa
        Escolha uma nova opção: '''
                      ))
    if opcao == 1:
        res = termo1 + termo2
        print(f'A soma de {termo1} e {termo2} é \033[1:31m{termo1 + termo2}\033[m.')
    elif opcao == 2:
        res = termo1 * termo2
        print(f'A multiplicação de {termo1} e {termo2} é \033[1:31m{termo1 * termo2}\033[m.')
    elif opcao == 3:
        if termo1 < termo2:
            res = termo2
            print(f'O número {termo2} é maior que o número {termo1}.')
        else:
            res = termo1
            print(f'O número {termo1} é maior que o número {termo2}.')
    elif opcao == 4:
        termo1 = int(input('Escolha o primeiro termo: '))
        termo2 = int(input('Escolha um segundo termo: '))
    elif opcao != 5:
        print('Por favor escolha uma das opções!')
print(f'\n\033[1mVocê escolheu sair do programa\033[m. Obrigado!')
