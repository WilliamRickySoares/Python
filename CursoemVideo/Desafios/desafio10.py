# Desafio 10
# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dolares ela pode comprar
# Considere US$ 1,00 = R$ 5,27

print('# Desafio 10'
      '\n# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira '
      'e mostre quantos Dolares ela pode comprar'
      '\n# Considere US$ 1,00 = R$ 3,27')

v = float(input('\nDigite quanto dinheiro há na carteira em reais (utilize ponto para decimais) >>> R$'))
c = float(5.67)
# Cotação no dia do desenvolvimento deste script é de 5.67 :(

print('\nHá na carteira R${:.2f}, com uma cotação de {:.2f} poderá comprar até US${:.2f}'
      .format(v, c, (v/c)))

# Aprimore o conversor para outras moedas, como Euro

print('Poderá comprar EU\u20ac{:.2f}'.format(v/6.33))
