# Desafio 023
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dígitos separados.
# Exemplo: "Digite um número: 1834
# Unidade: 4
# Dezena: 3
# Centena: 8
# Milhar: 1

n = int(input('Digite um número de 0 a 9999: '))
print('Analisando {}...'.format(n))
print('\nUnidade: {}'.format(n // 1 % 10))
print('Dezena: {}'.format(n // 10 % 10))
print('Centena: {}'.format(n // 100 % 10))
print('Milhares: {}'.format(n // 1000 % 10))

# FIXME: Não consegui fazer sozinho. Estudar a equação e entender a aplicabilidade
