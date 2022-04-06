"""
Desafio 041
A Conferederação Nacional de Natação precisa de um programa que
leia o ano de nascimento de um atleta e mostre sua categoria,
de acordo com a idade:
- Até 9 anos: MIRIM
- Até 14 anos: INFANTIL
- Até 19 anos: JUNIOR
- Até 20 anos: SÊNIOR
- Acima: MASTER
"""
from datetime import date

ano_nascimento = int(input('Digite o ano de nascimento do atleta: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
categoria = 'Indefinido'

if ano_nascimento >= ano_atual:
    print(f'Verifique o ano de \033[1:31m{ano_nascimento}\033[m digitado, '
          f'o ano de nascimento deve ser menor que \033[1:32m{ano_atual}\033[m.')
else:
    if idade <= 9:
        categoria = 'MIRIM'
    elif idade <= 14:
        categoria = 'INFANTIL'
    elif idade <= 19:
        categoria = 'JUNIOR'
    elif idade <= 20:
        categoria = 'SÊNIOR'
    elif idade > 20:
        categoria = 'MASTER'

    print(f'Considerando o ano \033[1m{ano_nascimento}\033[m do nascimento do atleta, '
          f'sua categoria é a \033[1:35m{categoria}\033[m para atletas de {idade} anos de idade!')
