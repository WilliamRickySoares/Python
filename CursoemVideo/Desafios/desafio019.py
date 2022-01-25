from random import choice

print('Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,'
      'lendo o nome deles e escrevendo o nome escolhido')

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

lista = [aluno1, aluno2, aluno3, aluno4]
print('O aluno escolhido foi {}'.format(choice(lista)))
