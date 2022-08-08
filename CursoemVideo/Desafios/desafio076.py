print("""
Desafio 076 (M3A16)
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
""")
tupla = ('Processador', '1.000,00', 'Placa mãe', '700,00', 'SSD 500mb', '500,00', 'HDD 500mb', '300,00'
         , 'Mouse', '30,00')

print('=' * 40)
print(f'{"Tabela de preços":^40}')
print('=' * 40)
for n in range(0, len(tupla)):
    if n % 2 == 0:
        print(f'{tupla[n]:.<27}', end='')
    if n % 2 != 0:
        print(f'R$ {tupla[n]:>10}')
print('=' * 40)
