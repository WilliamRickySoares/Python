"""
Desafio 039
Faça um programa que leia o ano de nascimento de uma jovem e informe,
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.
"""

idade = int(input('Digite a idade do jovem: '))
alistamento = int(18)

if idade > alistamento:
    print(f'A idade de alistamento é de {alistamento} e já passou {idade - alistamento} ano(s) da idade de se alistar')
elif idade < alistamento:
    print(f'A idade de alistamento é de {alistamento} e ainda faltam {alistamento - idade} ano(s) '
          f'para a idade de se alistar')
elif idade == alistamento:
    print(f'A idade de alistamento é de {alistamento} e está na idade de alistar. Faça sua parte!')
