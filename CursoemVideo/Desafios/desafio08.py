# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros

print('# Desafio 008 '
      '\n# Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros')

m = float(input('\nDigite o valor em metros >>> '))
c = m * 100
mm = m * 1000

print('\nO valor em metros digitado foi {}m, e esta medida em centímetros é {}cm e em milímetro é {}mm'
      .format(m, c, mm))
