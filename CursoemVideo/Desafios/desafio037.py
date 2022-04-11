"""
Desafio 037
Escreva um programa que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão

    - 1 para binário
    - 2 para octal
    - 3 para hexadecimal

TODO: Estudar bases numéricas
"""

num = int(input('Digite o número que pretende converter: '))
print('''Escolha a opção de conversão:
    -> 1 para binário
    -> 2 para octal
    -> 3 para hexadecimal
''')
opcao = int(input('Escolha uma opção: '))
res = 'uma opção incorreta, escolha entre 1, 2 ou 3.'
opc = 'um formato indefido'

if opcao == 1:
    # Modo 1: Utilizando um ponto especifico, iniciando do final para o começo, ou seja, os ultimos 8 digitos.
    # Serve para binário por causa da quantidade exata de dígitos
    res = bin(num)[2:]
    opc = 'BINÁRIO'
elif opcao == 2:
    # Modo 2: Desconsidera os primeiros (2) digitos e retorna todos os posteriores.
    res = oct(num)[2:]
    opc = 'OCTAL'
elif opcao == 3:
    # Modo 3: Substitui os caracteres ou trecho de caracteres por outro.
    # No caso, substitui 'Ox' (zero xis) por nada (aspas simples vazias)
    res = format(hex(num).replace('0x', ''))
    opc = 'HEXADECIMAL'

print('O número {} convertido para {} é {}'.format(num, opc, res))
