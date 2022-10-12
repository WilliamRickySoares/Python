"""Desafio 094
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
e todos os dicionários em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas com idade acima da média
"""

dic = {'qtd_pessoas': 0, 'soma_idade': 0, 'media_idade': 0}
pessoa = dict()
lista = list()
mulheres = list()
maiores = list()

while True:
    pessoa['nome'] = str(input("Digite o nome da pessoa: ")).strip().capitalize()
    while True:
        pessoa['sexo'] = str(input("Digite o sexo da pessoa [M/F]: ")).strip().upper()[0]
        if pessoa['sexo'] in "FfMm":
            break
        print('Digite apenas "M" ou "F"')
    pessoa['idade'] = int(input("Digite a idade da pessoa: "))
    lista.append(pessoa.copy())
    dic['pessoas'] = lista

    # a) Quantas pessoas foram cadastradas
    dic['qtd_pessoas'] += 1
    # b) A média de idade do grupo
    dic['soma_idade'] += pessoa['idade']
    dic['media_idade'] = dic['soma_idade'] / dic['qtd_pessoas']
    # c) Uma lista com todas as mulheres
    if pessoa['sexo'] in "Ff":
        mulheres.append(pessoa['nome'])
    dic['mulheres'] = mulheres
    while True:
        q = str(input("Quer continuar? [S/N] ")).strip().lower()[0]
        if q in "SsNn":
            break
        print('Por favor, escolher "Sim" ou "Não"')
    if q in "Nn":
        break
    print("")

# d) Uma lista com todas as pessoas com idade acima da média
for p in lista:
    if p['idade'] >= dic['media_idade']:
        maiores.append(p['nome'])
dic['maiores'] = maiores

print(f"Foram cadastradas {dic['qtd_pessoas']} pessoas.")
print(f"A média de idade é de {dic['media_idade']} anos. Considerando que {dic['soma_idade']} / {dic['qtd_pessoas']} "
      f"= {dic['media_idade']}.")
print(f"As mulheres cadastradas foram ", end = '')
for m in dic['mulheres']:
    print(m, end = '; ')
print(f"As pessoas acima da média foram {dic['maiores']}.")

print()
print(dic)
print()
