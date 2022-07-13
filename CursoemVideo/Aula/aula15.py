
'''
Nessa aula, vamos continuar a estudar os laços e vamos aprender a usar a estrutura de repetição while no Python. Por exemplo:
'''
# Exemplo
c = 1
while c != 10:
    print(c)
    c += 1
print('Acabou\n')

# Programa que pede um valor indefindamente, e pergunta se quer continuar ou não
r = 's'
while r == 's':
    n = int(input(f'Digite um número: '))
    r = str(input('Quer continuar? ')).lower()
print('Fim\n')

# Programa para digitar indefinidamente o valor, ao digitar um número específico (0 zero), encerra
num = 1
while num != 0:
    num = int(input('Digite um número: '))
print('Fim\n')


# Assistido em 12/07/2022