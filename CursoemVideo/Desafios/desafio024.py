# Desafio 024
# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

c = str(input('Digite o nome da cidades: ')).strip()
print('A cidade digitaca começa com "Santo": {}'.format('santo' in c.lower().split()[0]))
