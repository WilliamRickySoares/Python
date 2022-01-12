# Desafio 11
# Faça um programa que leia a largura e a altura de uma parede em metros,
# Calcule a sua área e a quantidade de tinta necessária para pintá-la,
# Sabendo que cada litro de tinda pinta uma área de 2 metros quadrados.

print('# Desafio 11'
      '\n# Faça um programa que leia a largura e a altura de uma parede em metros,'
      '\n# Calcule a sua área e a quantidade de tinta necessária para pintá-la,'
      '\n# Sabendo que cada litro de tinda pinta uma área de 2 metros quadrados.')

alt = float(input('\nDigite a altura (em metros) da parede >>> '))
lar = float(input('Digite a largura (em metros) da parede >>> '))
lit = float((alt * lar) / int(2))

print('\nUma parede de {} metros por {} metros de largura, é uma parede de {:.2f} metros quadrados.'
      .format(alt, lar, (alt * lar)))
if lit <= 1:
    print('Para pintar essa parede é necessário {:.2f} litro de tinta'.format(lit))
else:
    print('Para pintar essa parede são necessários {:.2f} litros de tinta'.format(lit))
