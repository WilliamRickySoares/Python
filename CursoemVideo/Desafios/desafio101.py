"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro
o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem
voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""


def voto(ano):
    from datetime import date
    situacao = ''
    ano_atual = date.today().year
    idade = ano_atual - ano_nascimento
    if idade < 16:
        return 'NEGADO'
    elif 16 <= idade < 18 or idade > 65:
        return 'OPCIONAL'
    if idade >= 18 <= 65:
        return 'OBRIGATÓRIO'


ano_nascimento = int(input("Digite o ano de nascimento: "))
print(f"Quem nasceu em {ano_nascimento}, o voto é {voto(ano_nascimento)}.")
