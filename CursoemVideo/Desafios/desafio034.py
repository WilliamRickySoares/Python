'''
Exercício Python 34:
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
'''

salario = float(input('\nQual o salário do funcionário? R$'))
if salario > 1250:
    percetual = 10
else:
    percetual = 15
print('\nO aumento salarial do funcionário é de \033[4m{}%\033[m, de \033[33mR${:.2f}\033[m passa para '
      '\033[1:32mR${:.2f}\033[m'.format(percetual, salario, salario + salario * (percetual/100)))
