print("""
Desafio 066
Digite um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando a flag).

""")

s = c = 0
while True:
    n = int(input('Digite um número (999 para sair): '))
    if n == 999:
        break
    s += n
    c += 1
print(f'Foram digitador {c} números cuja soma é {s}.')
