print("""
Desafio 070
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar.
No final, mostre:
a) Qual é o total gasto na compra.
b) Quantos produtos custam mais de R$ 1.000,00
c) Qual é o nome do produto mais barato.
""")

barato = perg = ''
soma = caro = menor = cont = 0

while True:
    prod = str(input('\nDigite o nome do produto: '))
    preco = float(input('Digite o valor do produto: '))

    # Item C
    if cont == 0 or preco < menor:
        barato = prod
        menor = preco

    # Item A
    soma += preco

    # Item B
    if preco > 1000:
        caro += 1

    # Enunciado
    cont += 1

    e = ' '
    while e not in 'SsNn':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if e in 'Nn':
        break

print(f'''
    Dentre os {cont} produtos:
    (a) o valor total da compra foi de R${soma:.2f} 
    (b) Há {caro} produtos com valor maior que R$ 1000,00 
    (c) O produto mais barato é o \033[1:33m{barato}\033[m que custa R${menor:.2f}''')
