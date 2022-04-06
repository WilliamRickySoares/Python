"""
Desafio 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela:
    - Abaixo de 18.5: Abaixo do peso
    - Entre 18.5 e 25: Peso ideal
    - 25 até 30: Sobrepeso
    - 30 até 40: Obsesidade
    - Acima de 40: Obseidade mórbida
"""

print('\n\033[1mCLACULADO DE IMC - ÍNDICIE DE MASSA CORPORAL\033[m')

peso = float(input('\nDigite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / altura
status = str('status')

if imc <= 18.5:
    status = str('Abaixo do peso')
elif imc < 25:
    status = str('Peso ideal')
elif imc < 30:
    status = str('Sobrepeso')
elif imc < 40:
    status = str('Obseidade')
elif imc > 40:
    status = str('Obseidade mórbida')

print(f'\nO seu imc é de {imc:.2f} com o status \033[1m{status}\033[m')
