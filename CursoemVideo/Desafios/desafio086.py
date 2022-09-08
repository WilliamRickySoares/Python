print("""Exercício 086
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
""")

# Solução 3 - Guanabara - Curso em Vídeo

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor [{linha}, {coluna}]: '))

print('\nResultado:\n')
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^6}]', end = '')
    print()


#  # Solução 1 - Com o resultado numa linha

posX = posY = 0
linha = int(input("\nQual a quantidade de colunas? "))
coluna = int(input("Qual a quantidade de colunas? "))
eixo = list()
matriz = list()
print("")

for x in range(0, linha):
    posX += 1
    posY = 0
    for y in range(0, coluna):
        posY += 1
        eixo.append(int(input(f"Digite um número [X = {posX}, Y = {posY}]: ")))
    matriz.append(eixo[:])
    eixo.clear()

print(matriz)
mont = 0
for a in matriz:
    print(matriz[mont])
    mont += 1
