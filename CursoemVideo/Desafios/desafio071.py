print("""
Desafio 071
Crie um programa que simule o financiamento de um caixa eletronico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

Obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
""")

saque50 = saque20 = saque10 = saque1 = troco = 0
valor = int(input('Digite o valor que deseja sacar: '))
if valor >= 50:
    saque50 = valor // 50
    troco = valor % 50
if troco > 0:
    saque20 = troco // 20
    troco = troco % 20
if troco > 0:
    saque10 = troco // 10
    troco = troco % 10
if troco > 0:
    saque1 = troco // 1
    troco = troco % 1


print(f'Serão entregues: '
      f'\n{saque50} notas de R$ 50,00'
      f'\n{saque20} notas de R$ 20,00'
      f'\n{saque10} notas de R$ 10,00'
      f'\n{saque1} notas de R$ 1,00')

