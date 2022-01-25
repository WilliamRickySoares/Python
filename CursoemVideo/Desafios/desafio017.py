import math

print('# Desafio 017'
      '\n# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo, '
      '\n  calcule e mostre o comprimento da hipotenusa')

co = float(input('\nQual o tamanho do cateto oposto: '))
ca = float(input('Qual o tamanho do cateto adjacente: '))
hi1 = (ca ** 2 + co ** 2) ** (1/2)
# ou importanto a bibilioteca
hi2 = math.hypot(co, ca)

print('\nO valor da hipotenusa é de {:.2f}'.format(hi2))
