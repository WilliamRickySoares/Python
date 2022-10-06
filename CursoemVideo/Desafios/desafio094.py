"""Desafio 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
"""

lista = dict()
pessoas = list()
mulheres = []
maiores = []

while True:
    lista['nome'] = str(input("Digite o nome da pessoa: ")).strip().capitalize()
    lista['sexo'] = str(input("Digite o sexo da pessoa [M/F]: ")).strip().lower()[0]
    lista['idade'] = int(input("Digite a idade da pessoa: "))
    pessoas.append(lista.copy())
    # lista['qtd_pessoas'] += 1
    # lista['soma_idade'] += lista['idade']
    # lista['media_idade'] = lista['soma_idade'] / lista['qtd_pessoas']
    # if lista['sexo'] in "Ff":
    #     mulheres.append(lista['nome'])

    while True:
        q = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
        if q in "SsNn":
            break
    if q in "Nn":
        break
    print("")

print(lista)
# print(lista['pessoas'])
