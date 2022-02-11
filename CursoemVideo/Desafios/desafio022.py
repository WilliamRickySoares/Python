# Desafio 022
# Crie um programa que leia o nome completo de uma pessoa e mostre:
# a. O nome com todos as letras maiusculas
# b. O nome com todas minusculas
# c. Quantas letras ao to do (sem considerar os espaços)
# d. Quantas letras tem o primeiro nome

nome = str(input('\nDigite o seu nome completo: ')).strip()
print('\nSeu nome em letas maiúscula: {}'.format(nome.upper()))
print('Seu nome em letas minuscula: {}'.format(nome.lower()))
print('Seu nome tem o total de {} letras, desconsiderando os espaços'
      .format(len(nome.replace(" ", ""))))
print('O primeiro nome {} e tem {} letras'.format(nome.split()[0], len(nome.split()[0])))
# segunda forma de fazer a linha anterior
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
