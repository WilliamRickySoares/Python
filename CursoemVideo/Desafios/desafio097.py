"""Desafio 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro
e mostre uma mensagem com tamanho adaptável.
"""


def escreva(text):
    t = len(text) + 4  # O mais 4 é para acrescentar a borda
    print(f"-" * t)  # O simbolo pode variar conforme escolha
    print(f"{text:^{t}}")  # Centralizado dinamicamente
    print(f"-" * t)


escreva("ue tenha uma função chamada escrev")
