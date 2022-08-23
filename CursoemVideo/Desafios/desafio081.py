print("""
Desafio 081
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma descrescente.
c) Se o valor 5 foi digitado e está ou não na lista.
""")

lista = []
while True:
    n = int(input("Digite um número inteiro: "))
    lista.append(n)

    q = ' '
    while q not in 'NnSs':
        q = str(input("Deseja adicionar mais números? [S/N] ")).strip().lower()[0]
    if q in 'Nn':
        break
# a
print(f"a) A lista possui {len(lista)} números digitados.")

# b
lista.sort(reverse = True)
print(f"b) A lista ordenada de forma descrescente: {lista}.")

# c
if 5 in lista:
    print(f'O número 5 está na posição {lista.index(5)}.')
else:
    print(f'O número 5 não está na lista!')

