
print("""
Fase 17 - LISTAS
""")

lanche = ['Hamburgue', 'Suco', 'Pizza', 'Pudim']
print(f'\nLista original: {lanche}')
lanche[3] = 'Picolé'
print(f"\nLista incluir item num index existente => lanche[3] = 'Picolé' => {lanche}")
lanche.append('Cookie')
print(f"\nLista insert 'cru' => lanche.append('Cookie') => {lanche}")
lanche.insert(0, 'Kikão')
print(f'\nLista insert na posição "lanche.insert(0, "Kikão")" => {lanche}')

del lanche[3]
lanche.pop(3)
lanche.remove("Kikão")

# Cria ou declara uma lista
lista1 = []
lista2 = list()



"""
Desafio 078
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas
respectivas posições na lista.

Desafio 079
Crie um programa onde o usuário possa digita vários valores e
cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.

Desafio 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta da inserção 
(sem usar o sort()).
No final, mostre a lista ordenada na tela.

Desafio 081
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados.
b) A lista de valores, ordenada de forma descrescente.
c) Se o valor 5 foi digitado e está ou não na lista.

Desafio 082
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os
valores pares e os valores impares digitados, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.

Desafio 083
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada
está com os parênteses abertos e fechados na ordem correta. 
"""