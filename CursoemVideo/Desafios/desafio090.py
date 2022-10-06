"""Desafio 090
Faça um programa que leia e média de um aluno, guardando tambem a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
"""

nome = str(input('Digite o nome do aluno: '))
media = float(input(f'Digte a média do {nome}: '))

boletim = dict()
boletim['nome'] = nome
boletim['media'] = media
boletim['ideal'] = 7.0
boletim['minimo'] = 5.0

if boletim['media'] >= boletim['ideal']:
    situacao = 'Aprovado'
elif boletim['media'] >= boletim['minimo']:
    situacao = 'em recuperação'
else:
    situacao = 'Reprovado'
boletim['situacao'] = situacao

print(boletim)

print(f"\nO aluno é o {boletim['nome']} e a situação é {boletim['situacao']}. Pois sua média é {boletim['media']:.1f}.")

