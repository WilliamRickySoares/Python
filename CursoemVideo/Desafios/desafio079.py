print("""Crie um programa onde o usuário possa digita vários valores e
cadastre-os em uma lista. Caso o número já exista lá dentro,
ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados,
em ordem crescente.""")

lista = []
q = ''

while q in 'NnSs':
    n = int(input(f'\nDigite um valor: '))
    if n not in lista:
        print(f'O número {n} foi adicionado a lista!')
        lista.append(n)
    else:
        print(f'O número {n} já está incluído na lista!')
    q = str(input('Deseja adicionar mais um número? [S/N] ')).strip().lower()[0]
    if q in 'Nn':
        break
lista.sort()
print(f'A lista digita foi {lista}')
