'''
# Desafio 013
# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.
'''

print('# Desafio 013 '
      '\n# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário com 15% de aumento.')

s = float(input('Qual o valor do salário? >>> R$'))
print('O valor do salário é de {:.2f}, adicionando 15%, ou seja R${:.2f}, totaliza R${:.2f}'
      .format(s, s * 15/100, s + s * 15/100))
