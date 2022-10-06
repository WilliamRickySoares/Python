#  Dicionários

# Formas de declarar
locadora = {}
# noinspection PyRedeclaration
locadora = dict()

# Exemplo:
# noinspection PyRedeclaration
locadora = {'Filme': 'Star Wars', 'Ano': 1977, 'Genero': 'Fantasia'}

print(locadora)
print(locadora['Filme'])
print(locadora['Ano'])
print(locadora['Genero'])

# Mostra a chave e o valor
print('\n', locadora.items())
for k, v in locadora.items():
    print(f'(items) O {k} é {v}')

# Mostra a chave (Key)
print('\n', locadora.keys())
for k in locadora.keys():
    print(f'(keys) {k}')

# Mostra o valor (values)
print('\n', locadora.values())
for v in locadora.values():
    print(f'(values) {v}')

# Dic original
pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 22}
print(f'\nDic completa de pessoas:\n{pessoas}')

# Adicionando mais uma posição
pessoas['peso'] = 98
print(f'Dic com adição de peso:\n{pessoas}')

# Removendo (deletando) uma posição específica
del pessoas['sexo']
print(f'Dic com remoção de sexo:\n{pessoas}')

# Apresentar um valor do dic
print(f'O nome é {pessoas["nome"]}')

# Adicionando dicionários à uma lista
print('\nAdicionando dicionários à uma lista')
brasil = []
estado1 = {'uf': 'Amazonas', 'sigla': 'AM'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(f'\nResultado da adição: \n{brasil}')

brasil.append({'uf': 'Estado', 'sigla': 'AQ'})

print(len(brasil))
print(f'\nResultado da adição: \n{brasil}')

estado = dict()
brasil = list()
for c in range(0, 3):
    estado['uf'] = str(input('Unidade feredativa: '))
    estado['sigla'] = str(input('Sigla do estado: '))
    # Ao final de cada laço, copiar os inputs para dentro da lista, o 'copy' não sobreescreve
    brasil.append(estado.copy())
print(brasil)

# DESAFIOS

"""Desafio 090
Faça um programa que leia e média de uma aluno, guardando tambem a situação em um dicionário. 
No final, mostre o conteúdo da estrutura na tela.
"""

"""Desafio 091
Crie um programa onde 4 jogadores joguem um dado e tenha resultados aleatórios. Guarde esses resultados num dicionário.
No final, coloque esse dicionário em ordem, sabedo que o vencedor tirou o maior número no dado.
"""

"""Desafio 092
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) num dicionário
se por acaso a CTPS for diferente de ZERO, o dicionário receberá tambem o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aponsentar.
"""

"""Desafio 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e 
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato. 
"""

"""Desafio 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionário em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas mulhes
d) Uma lista com todas as pessoas com idade acima da média
"""

"""Desafio 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluíndo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

"""Desafio 096
"""

"""Desafio 097
"""
