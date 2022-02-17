"""
Exercício Python 35:
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
"""

a = int(input('Digite o comprimento do primeiro lado: '))
b = int(input('Digite o comprimento do segundo lado: '))
c = int(input('Digite o comprimento do terceiro lado: '))

maior = c
if a > b and a > c:
    maior = a
elif b > a and b > c:
    maior = b

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

calc = a + b + c - menor - maior
triagulo = calc + menor
print(calc)
print(triagulo)
if triagulo > maior:
    print('\nAs medidas formam um triagulo')
else:
    print('\nAs medidas não formam um triangulo')
