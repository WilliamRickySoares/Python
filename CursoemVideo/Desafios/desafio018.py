from math import sin, cos, tan, radians


print('# Desafio 018'
      '\nFaça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, consseno'
      ' e tangente desse ângulo')

a = float(input('\nDigite um ângulo: '))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print('\nO ângulo de 30º tem o seno {:.2f}'.format(sen))
print('O ângulo de 30º tem o consseno {:.2f}'.format(cos))
print('O ângulo de 30º tem o tangente {:.2f}'.format(tan))
