"""
# Aula 013
# Desafio 056
Desenvolva um program que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
# - A média de idade do grupo;
- Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos;
"""
qtd = int(input('Qual a quantidade de pessoas: '))
cont = 0
mulheres20 = 0
total = 0
lista = []

for i in range(0, qtd):
    nome = str(input('\nDigite o nome da pessoa: '))
    idade = int(input('Digite a idade da pessoa: '))
    sexo = str(input('Digite o sexo da pessoa (M ou F): ')).lower()
    cont += 1
    total += idade
    if sexo == 'm':
        lista.append(idade)
    if sexo == 'f' and idade <= 20:
        mulheres20 += 1

media = total / cont


print(f'\nO homem com a maior idade tem {lista[0]} anos.')
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'Há {mulheres20} mulheres menor de 20 anos.')
