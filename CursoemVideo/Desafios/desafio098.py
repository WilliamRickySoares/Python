"""Desafio 098
Faça um programa que tenha uma função chamada contador(), que receba três parametros:
início, fim e passo e realize a contagem.
O seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, a cada um.
b) De 10 até 0, a cada dois.
c) Uma contagem personalizada.
"""

from time import sleep


def lin():
    print("-" * 35)


def contagem(i, f, c):
    lin()
    print(f"Contegem de {i} até {f} de {c} em {c}:")

    if i < f and c < 0 or i > f and c > 0:
        c *= -1

    if c == 0:
        c = 1

    if f < 0 or i > f:
        f += -1
    elif f > 0:
        f += 1

    count = 0
    for a in range(i, f, c):
        if count == 0:
            print(a, end = '')
        else:
            sleep(0.4)
            print(f", {a}", end = '')
        count += 1
    sleep(0.4)
    print(f".")
    sleep(0.4)
    print(f"Totalizando {count} números.")
    lin()
    print()

# main
contagem(1, 10, 1)
contagem(10, 0, 2)

inicio = int(input(f"Início: "))
final = int(input(f"Final:  "))
intervalo = int(input(f"Intervalo: "))
contagem(inicio, final, intervalo)
