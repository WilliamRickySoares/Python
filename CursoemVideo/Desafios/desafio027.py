# Desafio 027
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.
# Exemplo: Ana Maria de Souza
# Primeiro nome: Ana
# Último nome: Souza

nome = input('\nDigite seu nome completo: ')
print('Primeiro nome: {}'.format(nome.split()[0]))
print('Último nome: {}'.format(nome.split()[len(nome.split())-1]))
