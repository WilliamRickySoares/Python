print("""
Desafio 069
Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o program deverá perguntar se o usuário quer ou não continuar.
No final, mostre:
a) quantas pessoas tem mais de 18 anos.
b) Quantos homens foram cadastrados.
c) Quantas mulheres tem menos de 20 anos.
""")

cont = sexo = ''
total = maior = homens = mulher = 0

while True:
    idade = int(input('\nDigite a idade: '))
    sexo = str(input('Digite o sexo [F/M]: ')).strip().lower()[0]
    total += 1
    # a
    if idade > 18:
        maior += 1
    # b
    if sexo in 'Mm':
        homens += 1
    # c
    if idade < 20 and sexo in 'Ff':
        mulher += 1
    cont = str(input('Deseja continuar [S/N]? ')).lower().strip()[0]
    if cont in 'Nn':
        break
print(f'Foram cadastrados um total de {total} pessoa(s), {maior} tem mais de 18 anos, '
      f'{homens} são homem(ens) e há {mulher} mulher(es) com menos de 20 anos.')




