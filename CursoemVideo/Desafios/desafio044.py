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

print('''\n\033[1:33mFORMAS DE PAGAMENTO:\033[m
[ 1 ] À vista dinheiro / cheque
[ 2 ] À vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais no cartão''')
pgto = int(input('Escolha uma das opções de pagamento: '))

pago = 0

if pgto == 1:
    forma = 'à vista no dinheiro / cheque com 10% de desconto'
    pago = preco - preco * 0.10
    texto = 'e o valor pago deverá ser de R$ {:.2f}'.format(pago)
elif pgto == 2:
    forma = 'à vista no cartão com 5% de desconto'
    pago = preco - preco * 0.05
    texto = 'e o valor pago deverá ser de R$ {:.2f}'.format(pago)
elif pgto == 3:
    forma = 'parcelado em 2x no cartão sem juros'
    pago = preco * 1
    parc = 2
    texto = 'e o valor pago deverá ser em duas parcelas de R$ {:.2f}'.format(pago / 2)
elif pgto == 4:
    forma = 'parcelado em 3x ou mais no cartão com 20% de juros'
    pago = preco + preco * 0.20
    parc = int(input('Qual a quatidade de parcelas: '))
    texto = 'e o valor pago deverá ser de R$ {:.2f} em {} parcelas de R$ {:.2f}'.format(pago, parc, pago / parc)
else:
    pgto = ''
    forma = 'uma opção inválida'
    texto = ', no entanto \033[1:31mNÃO poderá ser pago nesta forma de pagamento\033[m.'

print('\nA forma de pagamento escolhida foi {}, '
      '\no valor original da compra é de R$ {:.2f} {}'.format(forma, preco, texto))
