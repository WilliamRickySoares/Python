"""Desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
O seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from random import randint
from time import sleep


def lin():
    print("-" * 90)


def maiorLista():
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


def maior(*n):
    num_maior = count = 0
    lin()
    for i in n:
        count += 1
        if i > num_maior:
            num_maior = i
    print(f"Foram digitados {count} números: {n}.")
    print(f"O maior número é {num_maior}.")
    lin()
    print()


# maiorLista()
maior(1, 2, 3, 20, 6, 4, 15, -52, 20, 17, 18)
maior(15, 12, 17, 18, 7, 25, -66, 4, 8, 9, 12, 5)
