"""Desafio 092
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) num dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá tambem o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aponsentar.
"""
from datetime import date
from time import sleep
think = '\nProcessando'
dot = '.'
t = 0

trabalhador = dict()

trabalhador['idade_aponsentadoria'] = 65
trabalhador['anos_contribuicao_minimo'] = 35
trabalhador['ano_atual'] = int(str(date.today())[0:4])

trabalhador['nome'] = str(input('Digite o nome: ')).strip().capitalize()
trabalhador['ano_nascimento'] = int(input('Digite o ano de nascimento: '))
trabalhador['idade'] = trabalhador['ano_atual'] - trabalhador['ano_nascimento']
trabalhador['anos_aposentadoria_faltantes'] = trabalhador['idade_aponsentadoria'] - trabalhador['idade']
trabalhador['num_ctps'] = int(input('Digite o número da CTPS (digite 0 quando não houver): '))
if trabalhador['num_ctps'] != 0:
    trabalhador['ano_contratacao'] = int(input('Digite o ano de contratação: '))
    trabalhador['anos_trabalhados'] = trabalhador['ano_atual'] - trabalhador['ano_contratacao']
    trabalhador['salario'] = float(input('Digite o salário: R$'))
    trabalhador['anos_contribuicao_faltantes'] = \
        trabalhador['anos_contribuicao_minimo'] - trabalhador['anos_trabalhados']

print(think, end='')
for i in range(1, 6):
    print(dot * 1, end='')
    sleep(0.4)


print("\n")
print(f"O contribuinte {trabalhador['nome']} possui atualmente {trabalhador['idade']} anos e poderá se aposentar por "
      f"idade em {trabalhador['anos_aposentadoria_faltantes']} anos, quando completar "
      f"{trabalhador['idade_aponsentadoria']} anos de idade.", end = ' ')
if trabalhador['num_ctps'] != 0 or '':
    print(f"Se trabalhou contribuindo desde {trabalhador['ano_contratacao']} já possui {trabalhador['anos_trabalhados']}"
          f" anos trabalhados e precisa de {trabalhador['anos_contribuicao_faltantes']} anos para completar os "
          f"{trabalhador['anos_contribuicao_minimo']} anos de contribuição por aponsentadoria por tempo de "
          f"serviço.", end = ' ')
    print(f"Por questões de cálculo o último salário foi R$ {trabalhador['salario']:.2f}.")

# for k, v in trabalhador.items():
#     print(f'{k}: {v}')

# print(f'\nDic completa: {trabalhador}\n')
