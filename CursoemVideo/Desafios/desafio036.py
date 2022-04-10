"""
Desafio 036:
Escreva um programa para aprovar o emprestimo bancário para a compra de uma casa.
O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação de mensal, sabendo que ela não pode esceder 30% do salário
ou então o empréstimo será negado
"""

valor_casa = float(input('Informe o valor do imóvel: '))
limite = 0.3 * float(input('Informe o valor do salário: '))
anos = int(input('Quantos anos para efetuar o pagamento: '))
parcela = valor_casa / (anos * 12)
if parcela > limite:
    print(f'\nA solicitação de emprestimo de R$ {valor_casa:.2f} foi \033[1:31mNEGADO\033[m.'
          f'\nO solicitante tem o limite de R$ {limite:.2f} '
          f'e o valor da parcela é de R$ {parcela:.2f}!')
else:
    print(f'\nA solicitação de emprestimo de R$ {valor_casa:.2f} foi \033[1:32mAPROVADO\033[m.'
          f'\nO solicitante tem o limite de R$ {limite:.2f} '
          f'e o valor da parcela é de R$ {parcela:.2f} por mês durante {anos} ano(s).')
