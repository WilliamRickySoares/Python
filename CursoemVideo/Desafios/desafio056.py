"""
# Aula 013
# Desafio 056
Desenvolva um program que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
# - A média de idade do grupo;
- Qual é o nome do homem mais velho;
# - Quantas mulheres têm menos de 20 anos;
"""
qtd = int(input('Qual a quantidade de pessoas: '))+1
mulheres20 = 0
total = 0
idoso = 0
nome_idoso = ''

for i in range(1, qtd):
    nome = str(input(f'\nDigite o nome da {i}º pessoa: '))
    idade = int(input(f'Digite a idade da {i}º pessoa: '))
    sexo = str(input(f'Digite o sexo da {i}º pessoa (M ou F): ')).lower()
    total += idade
    if sexo in 'Ff' and idade <= 20:
        mulheres20 += 1
    if sexo in 'Mm' and i == 1:
        idoso = idade
        nome_idoso = nome
    if sexo in 'Mm' and idade > idoso:
        idoso = idade
        nome_idoso = nome
media = total / qtd

print(f'\nO homem com a maior idade tem {idoso} anos e se chama {nome_idoso}.')
print(f'A média de idade do grupo é de {media:.1f} anos.')
print(f'Há {mulheres20} mulheres menor de 20 anos.')
