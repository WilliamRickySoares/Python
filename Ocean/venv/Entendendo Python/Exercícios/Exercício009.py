# Problema 6
# Crie um programa que gere um número inteiro aleatório entre 1 e 10.
# O programa deve então pedir ao usuário para adivinhar qual é esse número.
# Se o palpite do usuário estiver correto, o programa deve exibir uma mensagem de parabéns.
# Caso contrário, o programa deve informar se o número é maior ou menor que o palpite
# e dar ao usuário a chance de tentar novamente.
# O jogo deve seguir até o usuário adivinhar corretamente o número.

from random import randint
numero = randint(1,10)

while True:
    user = int(input("Adivinhe o número escolhido: "))
    if user > numero:
        print(f"Tente novamente, o número é menor")
    elif user < numero:
        print(f"Tente novamente, o número é maior")
    else:
        print("Parabéns você acertou!")
        break
