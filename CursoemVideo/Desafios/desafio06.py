# Desafio 006
# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

print('# Desafio 006 '
      '\n# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.')

n = int(input('\nDigite um número inteiro: '))
d = n * 2
t = n * 3
r = n ** (1/2)

print('\nO número digitado foi {} '
      '\n O dobro de {} é {} '
      '\n O triplo de {} é {} '
      '\n A raiz quadrada de {} é {:.}'
      .format(n, n, d, n, t, n, r))
