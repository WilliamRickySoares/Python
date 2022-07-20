print("""
Crie um programa que leia valores números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não
continuar a digitação valores.
"""
      )

i = True
soma = cont = 0
lista = []

while i:
    n = int(input('Digite valores inteiros: '))
    cont += 1
    soma += n
    lista.append(n)
    q = str(input(f'Deseja inserir mais valores? [S/N] ')).upper().strip()[0]
    if q in 'Nn':
        i = False

m = sorted(lista)
media = soma / cont
print(f'\nO maior valor da lista é o {m[-1]}')
print(f'O menor valor da lista é o {m[0]}')
print(f'Foram inseridos {cont} números.')
print(f'A soma dos números é de {soma}.')
print(f'A média total é de {media:.2f}.')
