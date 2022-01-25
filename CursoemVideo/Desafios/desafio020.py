from random import shuffle


print('\nO mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.'
      '\nFaça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada')

a = input('Primeiro aluno: ')
b = input('Segundo aluno: ')
c = input('Terceiro aluno: ')
d = input('Quarto aluno: ')

lista = [a, b, c, d]
shuffle(lista)
print('\nA sequencia de sorteio é {}'.format(lista))


