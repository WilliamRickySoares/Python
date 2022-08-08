print("""Desafio 075 (M3A16)
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares;\n""")


tupla = (int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')),
        int(input('Digite um número: ')))

print(f'\nA tupla digitada foi {tupla}.')

if 9 in tupla:
    print(f'a) O número 9 não foi digitado nessa tupla.')
else:
    print(f'a) O número 9 aparece {tupla.count(9)} vez.')

if 3 in tupla:
    print(f'b) O número 3 não foi digitado nessa tupla.')
else:
    print(f'b) O número 3 foi digitado na {tupla.index(3) + 1}º posição.')

print(f'c) Números pares digitados:', end=' ')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')
