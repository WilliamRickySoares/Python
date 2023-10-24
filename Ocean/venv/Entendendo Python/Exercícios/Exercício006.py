
# Aprimore o exemplo anterior de modo que o usuário possa inserir a quantidade de palavras que desejar.

quantidade_palavras = int(input("Quantas palavras quer adicionar: "))
lista = []
for palavra_adicionada in range(0, quantidade_palavras):
    palavra = input(f"Digite as palavras da lista {palavra_adicionada}: ")
    lista.append(palavra)

tamanho_limite = int(input("Qual o tamanho máximo de caracteres nas palavras: "))

for palavra in lista:
    if len(palavra) > tamanho_limite:
        print(f"A palavra {palavra} possui {len(palavra)} caracteres e ultrapassa o {tamanho_limite}.")

