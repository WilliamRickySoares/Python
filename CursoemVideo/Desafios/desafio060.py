'''
Faça um programa que leia um número qualquer
e mostre o seu fatorial.

Exemplo:
5! = 5x4x3x2x1 = 120
'''

n = int(input('Escolha um número para fatorar: '))

print(f'\033[1m{n}\033[m! =', end=' ')
factorial = int(1)
c = str('')

if n == 0:
    factorial = 1
for i in range(n, 0, -1):
    if i == n:
        factorial = n * 1
    else:
        factorial = i * factorial
    if i == 1:
        print(str(i), end=' = ')
    else:
        print(str(i), end=' x ')
print(f'\033[1:33m{factorial}\033[m.')

e = n
print(f'\n\033[1m{n}\033[m! =', end=' ')
while e != 0:
    if n == e:
        factorial = e * 1
    else:
        factorial = e * factorial
    if e == 1:
        print(str(e), end=' = ')
    else:
        print(str(e), end=' x ')
    e += -1
print(f'\033[1:33m{factorial}\033[m.')
