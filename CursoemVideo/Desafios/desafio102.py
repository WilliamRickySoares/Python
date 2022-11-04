"""
Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional)
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    n = 1
    for a in range(1, num + 1):
        n *= a
        if show:
            if a == num:
                print(a, end = ' = ')
            else:
                print(a, end = ' * ')
    print(n)


def somaExp(num, show=False):
    n = 0
    for a in range(1, num + 1):
        n += a
        if show:
            if a == num:
                print(a, end = ' = ')
            else:
                print(a, end = ' + ')
    print(n)


f = int(input("Digite o número fatorial: "))
fatorial(f, show = True)
somaExp(f, show = True)
