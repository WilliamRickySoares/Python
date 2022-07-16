'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Exemplo:
5! = 5x4x3x2x1 = 120
'''

n = int(input('Escolha um número para fatorar: '))

print(f'\033[1m{n}\033[m! =', end=' ')
f = int(1)
c = str('')

# Utilizando for (fiz antes do Guanabara solicitar :) rsrs )
if n == 0:
    f = 1
for i in range(n, 0, -1):
    if i == n:
        f = n * 1
    else:
        f = i * f  # f *= i
    if i == 1:
        print(str(i), end=' = ')
    else:
        print(str(i), end=' x ')
print(f'\033[1:33m{f}\033[m.')

# Utilizando while
e = n
print(f'\n\033[1m{n}\033[m! =', end=' ')
while e != 0:
    if n == e:
        f = e * 1
    else:
        f = e * f  # f *= e
    # if em uma única linha
    print(str(e), 'x ' if e > 1 else '= ', end='')
    e += -1
print(f'\033[1:33m{f}\033[m.')

# utilzando lib (math)
from math import factorial
print(f'\nO fatorial de {n} é \033[1:33m{factorial(n)}\033[m.')

# Modelo do Curso em Video - Guanabara
n = int(input('\nDigite um número para calcular seu Fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
