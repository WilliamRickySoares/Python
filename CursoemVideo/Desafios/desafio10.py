# Desafio 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# Considere US$ 1,00 = R$ 3,27

print('# Desafio 10'
      '\n# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira '
      'e mostre quantos Dolares ela pode comprar'
      '\n# Considere US$ 1,00 = R$ 3,27')

v = float(input('\nDigite quanto dinheiro há na carteira em reais (utilize ponto para decimais) >>> '))
c = float(3.27)

# Cotação no dia do desenvolvimento deste script é de 5.67 :(
d = v / c

print('\nHá na carteira R${:.2f}, com uma cotação de US${:.2f} e poderá comprar até US${:.2f}'
      .format(v, c, d))
