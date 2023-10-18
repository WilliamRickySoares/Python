"""
# Desafio 012
# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""

print('# Desafio 012 '
      '\n# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, '
      'com 5% de desconto.')

p = float(input('Qual o valor do produto? >>> R$'))
print('O valor do produto com desconto de 5%, ou seja R${:.2f}, fica no total R${:.2f} '.format(p * 5/100, p - p * 5/100))
