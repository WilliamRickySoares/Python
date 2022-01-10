# Desafio 07
# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média

print('# Desafio 07')
print('# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média')

n1 = float(input('\nDigite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
ns = float(n1+n2)
nm = float(ns / 2)

print('\nAs notas do aluno foram {:.2f} e {:.2f}, a soma é {:.2f} e a média atual é {:.2f}'.format(n1, n2, ns, nm))
