print("""
Exercício 087
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.
""")

total = terceira = segunda = pares = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        n = (int(input(f'Digite o número [{linha}, {coluna}] da matriz: ')))
        # Adiciona os numeros digitados na matriz
        matriz[linha][coluna] = n
        if n % 2 == 0:
            pares += n
        # Se a coluna for a 3º (no indicie a numero 2), então somar e incrementar
        if coluna == 2:
            terceira += n
        # Somar todos os numeros digitados e incrementar
        total += n
# Organizar a 2º linha (indice 1) de forma crescente
matriz[1].sort()
# Adiciona o ultimo valor (devido a ordenação é o maior valor) da linha 2 (indicie 1), a linha do meio
segunda = matriz[1][-1]

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end = '')
    print()

print(f'A soma de todos os números digitados é {total}.')
print(f'a) A soma dos valores pares é {pares}.')
print(f'b) A soma dos valores da terceira coluna é {terceira}.')
print(f'c) O maior valor da segunda linha é {segunda}')
