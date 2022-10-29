"""Desafio 100
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somarPar().
A primeira função vai sortear 5 números e vai colocar-los na lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""


def lin():
    print("-" * 60)


def sorteia():
    from random import randint
    sorteados = list()
    for i in range(0, 5):
        sorteados.append(randint(1, 10))
    lin()
    print(f"Os números sorteados foram: {sorteados}.")
    lin()
    return sorteados


def somaPar(listagem):
    soma = 0
    for p in listagem:
        if p % 2 == 0:
            soma += p
    lin()
    print(f"A soma dos pares dos números: {listagem} é {soma}.")
    lin()
    return soma


somaPar(sorteia())


