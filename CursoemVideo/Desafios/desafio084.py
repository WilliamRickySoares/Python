print("""Exercício 084
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.
d) (Adicional) Informar qual foi o menor e o maior peso.
""")
# TODO: Incrementar o tópico D da atividade

cad = list()
pessoas = []
pesados = list()
leves = list()
limite = float(input('Defina o limite de peso: '))


while True:
    pessoas.append(str(input("Nome da pessoa: ")).strip().capitalize())
    pessoas.append(float(input("Peso da pessoa: ")))

    if pessoas[1] >= limite:
        pesados.append(pessoas[0])
    else:
        leves.append(pessoas[0])
    pessoas.clear()

    q = ' '
    while q not in 'SsNn':
        q = str(input("Deseja continuar? [S/N] ")).strip().lower()[0]
    if q in 'Nn':
        break

print(f"\na) Foram cadastrados {len(leves) + len(pesados)} pessoas.")

print(f"b) As pessoas mais pesados são ", end = '')
for p in pesados:
    if p == pesados[-1]:
        print(f'{p}.')
    else:
        print(f'{p}, ', end = '')

print(f"c) As pessoas mais leves são ", end = '')
for a in leves:
    if a != leves[-1]:
        print(f'{a}, ', end = '')
    else:
        print(f'{a}.')
