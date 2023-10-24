
# Escreva um programa que percorra uma lista de palavras
# e exibe aquelas que possuem um comprimento maior do que um determinado valor.

lista = ['casa', 'bolacha', 'computador']
tamanho_limite = int(input("Determinte um valor de caracteres: "))

for palavra in lista:
    if len(palavra) > tamanho_limite:
        print(f"A palavra {palavra.upper()} possui {len(palavra)} caracteres e ultrapassa o {tamanho_limite}.")
