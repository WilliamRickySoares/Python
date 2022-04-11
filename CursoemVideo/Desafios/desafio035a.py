"""
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""
# Uma segunda forma de fazer, idealizado por William Soares

a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))

if a + b > c and a + c > b and b + c > a:
    print('\nAs medidas \033[1:32mPODE FORMAR\033[m um triagulo')
else:
    print('\nAs medidas \033[1:31mNÃO PODE FORMAR\033[m um triângulo')
