print('\n# Desafio 014 \n# Faça um programa que converta uma temperatura digita em ºC e converta para ºF')

c = float(input('\nDigite a temperatura em graus Celsus: '))
f = c * 1.8 + 32 # ou c * 9 / 5 + 32
k = c + 273
print('\nA temperatura de {:.2f}ºC, convertido para Fahrenheit é de {:.2f}ºF.'.format(c, f))
print('A mesma temperatura em Kelvis é de {:.2f}ºK'.format(k))
