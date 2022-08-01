"""
Curso de Python #15 - Interrompendo repetições while


EXPLICAÇÂO:
Quando houver a necessidade de validações específicas para sair do while, o termo 'break' é utilizado
Caso quando a consição do break é atendida, o script sai da repetição das estruturas de controle.
"""

# Exemplo 1
pedra = vazio = moeda = 1
trofeu = 1

while True:
    if pedra == 1:
        print(f'\nQuando houver um bloco preenchido, O personagem anda')
    if vazio == 1:
        print(f'Quando houver um bloco vazio, o personagem pula')
    if moeda == 1:
        print(f'Quando houver moeda, o personagem pega a moeda')
    if trofeu == 1:
        print(f'Quando houver trofeu, o personagem pega o trofeu')
        break
print('\nO personagem pega a maça')

# Exemplo 2

n = s = 0
while True:
    n = int(input('Digite o número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print(f'A soma vale {s}')

"""
Desafio 066
Digite um programa que leia vários números inteiros pelo teclado.
O programa só vai para quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados
e qual foi a soma entre eles (desconsiderando a flag).

Desafio 067
Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

Desafio 068
Faça um programa que jogue par ou impar com o computador. O jogo só será interrompido quando o jogador PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

Desafio 069
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o program deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.

Desafio 070
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1.000,00
c) Qual é o nome do produto mais barato.

Desafio 071
Crie um programa que simule o financiamento de um caixa eletronico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""