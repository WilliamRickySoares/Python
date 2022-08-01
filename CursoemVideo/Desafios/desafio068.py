from random import randint

print("""
Desafio 068
Faça um programa que jogue par ou impar com o computador. 
O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
""")


# Formatar design
print('==' * 15)
print('   Vamos jogar PAR ou IMPAR')
print('==' * 15)
c = 0

while True:
    # Usuário escolhe as opções
    j = int(input('\nEscolha um número: '))

    # Formatar a escolha do jogador
    while True:
        e = str(input('Escolha entre Par ou Impar [P/I]: ')).strip().upper()[0]
        if e in 'Pp':
            escolhido = 'par'
        elif e in 'In':
            escolhido = 'impar'
        break

    # Sortear e formatar a escolha do código
    n = randint(1, 10)
    soma = n + j
    r = soma % 2
    if r == 0:
        tipo = 'par'
    else:
        tipo = 'impar'

    # Verificar se o jogador ganhou
    if r == 0 and e in 'Pp' or r == 1 and e in 'Ii':
        d = 'VENCEU'
        ganhador = True
        c += 1
    else:
        d = 'PERDEU'
        ganhador = False
        # print(d)
        # revanche = str(input('\nDeseja jogar novamente? ')).strip().upper()[0]
        # if revanche in 'NAO' or revanche in 'NÃO':
    print(f'Você escolheu {escolhido} e o resultado foi {soma} ({tipo}), você \033[1:33m{d}\033[m!')

    # Se o jogador perdeu, encerrar!
    if not ganhador:
        break
print(f'\nVocê ganhou {c} vezes consecutivas.')
