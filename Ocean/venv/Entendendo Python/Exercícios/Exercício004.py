# Exercício 004
#Problema 01

# Identificar a quantidade de letas 'a' tem na palavra digitada

palavra = str(input("Digite uma palavra: "))
quantidade_a = 0

for letra in range(0, len(palavra)):
    if palavra[letra].lower() == 'a':
        quantidade_a += 1

# Solução do instrutor (Melhor)
# for letra in palavra:
#     if letra == 'a':
#         quantidade_a += 1

print(f"Na palavra {palavra} há {quantidade_a} vezes a letra 'a'.")
