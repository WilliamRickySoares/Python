from math import trunc


print('\nDesafio 016'
      '\nCrie um programa que leia um número Real qualquer pelo teclado e mostre a sua porção inteira')

f = float(input('Digite o número decimal >>> '))
print('O {1} é a parte inteira de {0}.'.format(f, trunc(f)))
# ou sem importar módulos (math)
print('O {1} é a parte inteira de {0}.'.format(f, int(f)))
