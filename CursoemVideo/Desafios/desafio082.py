print("""Desafio 082
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.""")

lista = []

while True:
    n = int(input("\nDigite um número inteiro: "))
    lista.append(n)

    e = ' '
    while e not in 'SsNn':
        e = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if e in 'Nn':
        break

impar = []
par = []
for i in lista:
    if i % 2 == 0:
        par.append(i)
    elif i % 2 != 0:
        impar.append(i)

print("\n")
print("*" * 40)
print(f"Lista digitada > {lista}")
print(f"Números pares digitados > {par}")
print(f"Números impares digitados > {impar}")
print("*" * 40)
