print("""Exercício 085
Crie um programa onde o usuário possa digitar 7 valores 
numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares. No final, 
mostre os valores pares e impares em ordem crescente.
""")

listagem = [[], []]
for i in range(0, 4):
    valor = int(input("Digite o número: "))
    if valor % 2 == 1:
        listagem[0].append(valor)
    else:
        listagem[1].append(valor)

print(f'Os valores impares são {listagem[0].sort()}')
print(f'Os valores pares são {listagem[1].sort()}')
