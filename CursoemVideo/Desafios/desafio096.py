"""Desafio 096
Faça um programa que tenha uma função chamada área(), que receba oas dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""


def lin(simbol):
    print(f"{simbol}" * 35)


def area():
    print("Calculadora de terrenos")
    lin("-")
    lar = float(input(f"Insera a largura do terreno: "))
    com = float(input(f"Insera o comprimento do terreno: "))
    a = lar * com
    lin("=")
    print(f"O terreno medindo {lar:.1f} metros por {com:.1f} metros possui uma área de {a:.1f} metros quadrados.")
    lin("=")


area()
