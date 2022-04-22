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
print('\n[ 1 ] À vista dinheiro / cheque: 10% de desconto')
print('[ 2 ] À vista no cartão: 5% de desconto')
print('[ 3 ] Em até 2x no cartão: preço normal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
pgto = int(input('Escolha uma opção de pagamento: '))


if pgto == 1:
    pago = preco - preco * 0.10
elif pgto == 2:
    pago = preco - preco * 0.05
elif pgto == 3:
    pago = preco * 1
elif pgto == 4:
    pago = preco + preco * 0.20

print('\nO valor pago será de R$ {:.2f}!'.format(pago))
