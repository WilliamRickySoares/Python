"""
Desafio 039
Faça um programa que leia o ano de nascimento de uma jovem e informe,
de acordo com a sua idade:
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou o que passou do prazo.
Se for Homem, senão informe que não é necessário
"""

from datetime import date

ano_atual = date.today().year
genero = str(input('Insira a abreveação do gênero, utilize [f] para feminino e [m] para marculino: '))

if genero.lower() == 'f':
    print('No Brasil, mulheres não tem obrigação de alistar')
elif genero.lower() == 'm':
    ano_nascimento = int(input('Insira o ano de nascimento do candidato: '))
    dif = ano_atual - ano_nascimento
    if dif == 18:
        print('Os candidatos nascidos em {} deverão se apresentar para alistamento neste ano de {}.'
              .format(ano_nascimento, ano_atual))
    elif dif > 18:
        print('Os candidatos nascidos em {} passaram {} anos da idade de alistar, '
              'procure a junta militar se não foi realizado o alistamento'
              .format(ano_nascimento, (ano_atual - ano_nascimento) - 18))
    elif dif < 18:
        print('Os candidatos nascidos em {} deverão aguardar {} anos, até {} para se apresentar para o alistamento'
              .format(ano_nascimento, (ano_nascimento + 18) - ano_atual, ano_nascimento + 18))
    elif dif <= 0:
        print('O ano {} não é válido para verificação'.format(ano_nascimento))
else:
    print('\n"{}" não é um genero válido, utilize [f] para feminino e [m] para marculino.'.format(genero))
