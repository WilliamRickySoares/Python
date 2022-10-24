"""Desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
O seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def lin():
    print("-" * 93)


def maiorLista():
    from random import randint
    from time import sleep
    v = randint(1, 5)
    for c in range(v):
        n = randint(2, 10)
        a = list()
        for i in range(0, n):
            a.append(randint(1, 50))

        # Titulo
        lin()
        print("Gerando valores", end = '')
        for p in range(0, 5):
            sleep(0.3)
            print(".", end = '')
        # Apresentando os numeros
        print(f"\nForam sorteados {n} números {a}", end = '')
        # Ordenando
        a.sort()
        print(f" e o maior é o número {a[-1]}.")
    lin()


maiorLista()

