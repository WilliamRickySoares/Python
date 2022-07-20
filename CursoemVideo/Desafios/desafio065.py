print("""
Crie um programa que leia valores números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não
continuar a digitação valores.
"""
      )

soma = cont = maior = menor = 0
r = 'S'
while r in 'Ss':
    n = int(input('Digite valores inteiros: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    r = str(input(f'Deseja inserir mais valores? [S/N] ')).upper().strip()[0]

media = soma / cont
print(f'\nO maior valor da lista é o {maior}.')
print(f'O menor valor da lista é o {menor}.')
print(f'Foram inseridos {cont} números.')
print(f'A soma dos números é de {soma}.')
print(f'A média total é de {media:.2f}.')
