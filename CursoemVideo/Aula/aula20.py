"""
Aula 20 = Funções
"""
# Para criar rotinas que podem ser chamadas várias vezes


# Criar uma função que crie uma linha quando for chamada.
def lin():
    print("-" * 30)

lin()
print("Texto A")
lin()

lin()
print("Texto B")
lin()

lin()
print("Texto C")
lin()

# Funcão com parametro
def mensagem(msg):
    print("-" * 30)
    print(msg)
    print("-" * 30)

print()
# Chama / Executa a função, informando o parametro que será utlizado na função
mensagem("Texto D")
mensagem("Texto E")

# Declarando parametros numa função
def soma(a, b):
    print()
    lin()
    print(f"O resultado da soma {a} de e {b}")
    s = a + b
    print(f"O resultado é igual a {s}")

soma(b=4, a=5)
soma(7, 2)


# Quando não souber a quantidade de parametros, incluir um asterisco antes do parametro na função
def contador(* num):
    tam = len(num)
    print()
    lin()
    print(f"Recebido os valores {num} no total de {tam} números.")


contador(1)
contador(2, 3)
contador(4, 5, 6)
contador(7, 8, 9, 10)


# Utilizando uma lista como parametro
def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print()
lin()
print(valores)


# Desempacotando e usando lista
def somaLista(* valores):
    """
    Informar vários parametros separados por virgula.

    Declação:
    somaLista(n1, n2, n, ...)
    """
    s = 0
    for num in valores:
        s += num
    print(f"Somando os valores {valores} temos {s}.")

print()
lin()
somaLista(5, 2)
somaLista(2, 9, 4)


"""Desafio 096
Faça um programa que tenha uma função chamada área(), que receba oas dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
"""

"""Desafio 097
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parametro
e mostre uma mensagem com tamanho adaptável.
"""

"""Desafio 098
Faça um programa que tenha uma função chamado contador(), que receba três parametros:
início, fim e passo e realize a contagem.
Seu programa tem que realizar três contagens através da função criada:

a) De 1 até 10, de em 1
b) De 10 até 0, de 2 em 2
c) Uma contagem personalizada.
"""

"""Desafio 099
Faça um programa que tenha uma função chamada maior(), que receba vários parametros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""

"""Desafio 100
Faça um programa que tenha uma lista chamada numeros e duas funções chamadas sorteia() e somarPar().
A primeira função vai sortear 5 números e vai coloca-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores PARES sorteados pela função anterior.
"""
