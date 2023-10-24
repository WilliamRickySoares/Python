# Exercicio 3

# dada a tabela o IR, faça um programa que recebe o salário de um trabalhador e devolve o valor do imposto.
# Utilizando a regra de imposto efetiva até 2021

# #|Base de cálculo (R$) |Alíquota (%)|
# #--------------------- |-------------|
# #|Abaixo de 1.903,98 | 0% |
# #|De 1.903,99 até 2.826,65| 7,5% |
# #|De 2.826,66 até 3.751,05| 15% |
# #|De 3.751,06 até 4.664,68| 22,5% |
# #|Acima de 4.664,69 | 27,5% |

valor_salario = float(input("Valor do salário: "))
alicota = 0
if valor_salario <= 1903.98:
    alicota = 0
elif valor_salario >= 1903.99 and valor_salario <= 2826.65:
    alicota = 7.5
elif valor_salario >= 2826.66 and valor_salario <= 3751.05:
    alicota = 15.0
elif valor_salario >= 3751.06 and valor_salario <= 4664.68:
    alicota = 22.5
elif valor_salario >= 4664.69:
    alicota = 27.5

print(f"A alicota a ser paga é de {alicota}%, sob o valor do salario de R$ {valor_salario:.2f}")
print(f"Valor a pagar R$ {valor_salario * alicota:.2f}")
