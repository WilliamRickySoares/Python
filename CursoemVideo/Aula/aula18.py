pessoas = [['Pedro', 25], ['Maria', 19], ['João', 32]]

print(pessoas[0])     # imprime ['Pedro', 25]
print(pessoas[0][0])  # imprime 'Pedro'
print(pessoas[0][1])  # imprime 25
print(pessoas[1])     # imprime ['Maria', 19]
print(pessoas[1][0])  # imprime 'Maria'
print(pessoas[1][1])  # imprime 19
print(pessoas[2])     # imprime ['João', 32]
print(pessoas[2][0])  # imprime 'João'
print(pessoas[2][1])  # imprime 32

teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
# A adição dos dois pontos entre colchetes permite não vincular uma lista a outra, criando uma nova

teste[0] = 'Maria'
teste[1] = 19
galera.append(teste[:])  # Adicionar colchetes para criar uma nova lista sem vinculo a anterior

# print(aluno)
print(f"Galera = {galera}")

# Printar cada elemento conforme o indicie:
for p in galera:
    print(f'O {p[0]} tem {p[1]} anos')

turma = list()
dado = list()
# for c in range(0, 3):
#     dado.append(str(input('Nome: ')))
#     # Inserir o valor do input diretamente na lista
#     dado.append(int(input('Idade: ')))
#     turma.append(dado[:])
#     # Copia (como: usando os colhetes a lista que foi preenchida
#     # para outra lista (Como: usando appent)
#     dado.clear()
#     # Excluir os dados da lista (Como: clear() )

print(dado)
print(turma)

for p in turma:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')

print("""
Exercício 084
Faça um progrma que leia nome e peso de várias pessoas, 
guardando tuo em uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas.
b) Uma listagem com as pessoas mais pesadas.
c) Uma listagem com as pessoas mais leves.

Exercício 085
Crie um programa onde o usuário possa digitar 7 valores 
numéricos e cadastre-os em uma lista única
que mantenha separados os valores pares e impares. No final, 
mostre os valores pares e impares em ordem crescente.

Exercício 086
Crie um programa que crie uma matriz de dimensão 3x3 e 
preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.

Exercício 087
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados.
b) A soma dos valores da terceira coluna.
c) O maior valor da segunda linha.

Exercício 088
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos seráo gerados 
e vai sortear 6 números entre 1 e 60 para cada jogo, 
cadastrando tudo em uma lista composta.

Exercício 089
Crie um programa que leia nome e duas notas de vários alunos 
e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita 
que o usuário possa mostrar as notas de cada aluno individualmente.

""")
