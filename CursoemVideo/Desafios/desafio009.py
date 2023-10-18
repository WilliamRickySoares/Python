# Desafio 009
# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

print('# Desafio 009 \n# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.')

n = int(input('\nDigite o número da tabuada >>> '))
n0 = n+0
n1 = n+1
n2 = n+2
n3 = n+3
n4 = n+4
n5 = n+5
n6 = n+6
n7 = n+7
n8 = n+8
n9 = n+9
n10 = n+10

print('\nA tabuada de adição de {} é:'
      '\n{} + 0 = {}'
      '\n{} + 1 = {}'
      '\n{} + 2 = {}'
      '\n{} + 3 = {}'
      '\n{} + 4 = {}'
      '\n{} + 5 = {}'
      '\n{} + 6 = {}'
      '\n{} + 7 = {}'
      '\n{} + 8 = {}'
      '\n{} + 9 = {}'
      '\n{} + 10 = {}'
      .format(n, n, n0, n, n1, n, n2, n, n3, n, n4, n, n5, n, n6, n, n7, n, n8, n, n9, n, n10))
# Jeito errado /\

# Jeito certo  \/
print('-'*15)
print('\nA tabuada de multipliação de {} é:')
print('{} * {} = {}'.format(n, 0, n*0))
print('{} * 1 = {}'.format(n, n*1))
print('{} * 2 = {}'.format(n, n*2))
print('{} * 3 = {}'.format(n, n*3))
print('{} * 4 = {}'.format(n, n*4))
print('{} * 5 = {}'.format(n, n*5))
print('{} * 6 = {}'.format(n, n*6))
print('{} * 7 = {}'.format(n, n*7))
print('{} * 8 = {}'.format(n, n*8))
print('{} * 9 = {}'.format(n, n*9))
print('{} * {} = {}'.format(n, 10, n*10))
