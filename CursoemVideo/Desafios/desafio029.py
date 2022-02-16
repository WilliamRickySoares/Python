'''
Exercício Python 29:
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
'''

v = float(input('Digite a velocidade de um carro: '))
if v > 80:
    print('\nVoce foi multado em\033[31m R$ {:.2f}\033[m por ultrapassar em \033[33m{:.2f}Km\033[m!'.format( (v-80)*7, v-80))
print('\n\033[32mDigira sempre com cuidado, use cinto de segurança!\033[m')
