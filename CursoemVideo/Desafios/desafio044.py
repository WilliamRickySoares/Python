"""
Desafio 044
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço e a condição de pagamento:
    - À vista dinheiro / cheque: 10% de desconto
    - À vista no cartão: 5% de desconto;
    - Em até 2x no cartão: preço normal
    - 3x ou mais no cartão: 20% de juros
"""

preco = float(input('Digite o valor do produto: '))
print('\n\033[1mAs opções de pagamento são:\033[m')
print('[ 1 ] À vista dinheiro / cheque: 10% de desconto')
print('[ 2 ] À vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2x no cartão: preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
pgto = int(input('Escolha uma das opções de pagamento: '))
forma = 'uma opção inválida'
pago = 0

if pgto == 1:
    forma = 'à vista no dinheiro / cheque com 10% de desconto'
    pago = preco - preco * 0.10
elif pgto == 2:
    forma = 'à vista no cartão com 5% de desconto'
    pago = preco - preco * 0.05
elif pgto == 3:
    forma = 'parcelado em 2x no cartão sem juros'
    pago = preco * 1
elif pgto == 4:
    forma = 'parcelado em 3x ou mais no cartão com 20% de juros'
    pago = preco + preco * 0.20
else:
    pgto = ''

print('\nA forma de pagamento escolhida foi de {} e o valor pago deverá ser de R$ {:.2f}!'.format(forma, pago))
