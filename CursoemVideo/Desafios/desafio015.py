print('\n# Desafio 015 \n# Escreva um programa que pergunte a quantidade de Km percorridos por um carro'
      ' alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, '
      'sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.')

d = int(input('\nPor quantos dias o carro foi alugado? >>> '))
k = float(input('Quantos quilometros o carro rodou? >>> '))
custo_dias = d * 60
custo_km = k * 0.15
custo = custo_km + custo_dias

print('\nO carro foi alugado por {} dias e gerou o custo de R${:.2f}, '
      'rodando {} km durante esse periodo gerando o custo de R${:.2f}. '
      '\nQue gerou o custo total de R${:.2f} a pagar.'
      .format(d, custo_dias, k, custo_km, custo))
