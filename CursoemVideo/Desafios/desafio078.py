print("""
Desafio 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.
""")

lista = []
menores = []
maiores = list()

for i in range(0, 5):
    n = int(input(f"Digite um número [{i}]: "))
    lista.append(n)

ordenada = lista[:]
ordenada.sort()
menor = ordenada[0]
maior = ordenada[-1]

for c, v in enumerate(lista):
    if v == menor:
        menores.append(c)
    if v == maior:
        maiores.append(c)
print(f'O menor valor é {menor} e está na posição {menores}')
print(f'O maior valor é {maior} e está na posição {maiores}')

