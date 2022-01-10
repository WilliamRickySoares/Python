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
area = alt * lar
efi = int(2)
lit = float(area / efi)

print('\nA altura da parede é de {} metros, a largura é de {} metros, a área da parede é de {} metros quadrados.'
      .format(alt, lar, area))
if lit <= 1:
    print('Para pintar essa parede é necessário {:.2f} litro de tinta'.format(lit))
else:
    print('Para pintar essa parede são necessários {:.2f} litros de tinta'.format(lit))
