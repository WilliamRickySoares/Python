print("""Exercício 089
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar 
as notas de cada aluno individualmente.
""")

aluno = list()
chamada = 1
while True:
    nome = str(input('Qual o nome do aluno: ')).strip().lower()
    nota1 = float(input(f'Digite a 1º nota do {nome.capitalize()}: '))
    nota2 = float(input(f'Digite a 2º nota do {nome.capitalize()}: '))
    media = (nota1 + nota2) / 2

    aluno.append([nome, [nota1, nota2], media, chamada])
    chamada += 1

    q = ' '
    while q not in 'SsNn':
        q = str(input('Deseja continuar: [S/N] ')).strip().lower()[0]
    if q in 'Nn':
        break

print('\n------------ BOLETIM ------------')
print(f'{"Chamada":<8}{"Nome":<15}{"Média":>8}')
for i in aluno:
    print(f'{i[3]:<8}{i[0].capitalize():<15}{i[2]:>7.1f}')

while True:
    x = str(input(f'\nQual o número do aluno que deseja visualizar o boletim? ')).strip().lower()
    cont = 0
    for u, a in enumerate(aluno):
        if x in a[0]:
            cont += 1
            ind = u
    if cont > 0:
        print(f'A nota do aluno(a) foi {aluno[ind][0].capitalize()} foi de {aluno[ind][1][0]:.2f} '
              f'e {aluno[ind][1][1]:.2f}, totalizando {(aluno[ind][1][0] + aluno[ind][1][1]):.2f}, '
              f'com média de {aluno[ind][2]:.1f}!')
    else:
        print(f'O aluno {x.capitalize()} não foi localizado no boletim')

    continuar = ' '
    while continuar not in 'SsNn':
        continuar = str(input('Deseja consultar outro aluno? [S/N] ')).strip().lower()[0]
    if continuar in 'Nn':
        print('Finalizado!')
        break
