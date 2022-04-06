"""
Desafio 040
Crie um programa que leia duas notas de um aluno e calcule sua média,
mostrando uma mensagem no final, de acordo com a média atingida:
- Média abaixo de 5.0: REPROVADOR
- Média entre 5.0 e 6.9: RECUPERAÇÃO
- Média 7.0 ou superior: APROVADOR
"""

n1 = float(input('Digite a primeira nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
med = (n1 + n2) / 2

if med >= 7:
    print(f'O aluno teve as notas {n1:.2f} e {n2:.2f} gerando uma média de {med:.2f}, '
          f'então está \033[1:32mAPROVADO\033[m.')
elif med < 5:
    print(f'O aluno teve as notas {n1:.2f} e {n2:.2f} gerando uma média de {med:.2f}, '
          f'então está \033[1:31mREPROVADO\033[m.')
else:
    print(f'O aluno teve as notas {n1:.2f} e {n2:.2f} conseguindo uma média de {med:.2f}, '
          f'então está \033[1:35mRECUPERAÇÃO\033[m')
