"""
Desafio 042
Refaça o Desafio 035 dos triangulos,
acrescentando o recurso de mostrar que tipo de triângulo será formado:
    - Equilátero: todos os lados iguais
    - Isósceles: dois lados iguais
    - Escaleno: todos os lados diferentes
"""

a = float(input('Digite o primeiro comprimento: '))
b = float(input('Digite o segundo comprimento: '))
c = float(input('Digite o terceiro comprimento: '))
tri = 'Escaleno'

if a == b == c:  # forma alternativa a == b and b == c and a == c
    tri = 'Equilátero'
elif a == b or a == c or b == c:  # forma alternativa, utilizar essa condição no 'else'
    tri = 'Isósceles'
elif a != b != c != a:  # forma alternativa a != b and b != c and a != c
    tri = 'Escaleno'

if a + b > c and a + c > b and b + c > a:
    print('\nAs medidas \033[1:32mPODE FORMAR\033[m um triagulo', end='')
    print(' do tipo \033[4:1m{}\033[m.'.format(tri))
else:
    print('\nAs medidas \033[1:31mNÃO PODE FORMAR\033[m um triângulo')
