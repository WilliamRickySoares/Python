"""
# Aula 013
# Desafio 053
Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços.
Exemplos de palíndromo:
    "APOS A SOPA",
    "A SACADA DA CASA"
    "A TORRE DA DERROTA"
    "O LOBO AMA O BOLO"
    "ANOTARAM A DATA DA MARATONA"
"""

frase = str(input('Digite a frase: '))
phase = (frase.strip().upper().replace(" ", ""))
m = len(phase)
t = 0
inverso = ''

# Solução 1 usando o tamanho do frase e construindo a frase invertida a cada iteração
for letra in range(m-1, -1, -1):
    inverso += phase[letra]

# Soluçõa 2 usando a comparação de cada letra contanddo da apartir da esquerda e o mesmo da direita.
# A cada iteração é validado se ambas a letras são iguais
# Validando se a quantidade de letras iguais é igual ao total de letras da frase, ou se,
# Validando se há letras divergentes, havendo ao menos 1 já considera false (não é palindromo)
for c in range(0, m):
    i = 0 + c
    f = m - (c + 1)
    if phase[i] == phase[f]:
        t += 1

# Solução 3 utilizando a leitura de string de traz pra frente
inv = phase[::-1]
print(inv)

if t == m and inverso == phase:
    print(f'\nOs caraceteres posicionados inversamente geram a mesma frase "' + f'{inverso}' + '", ou seja,'
                                                                                               f' {frase} é um \033[1:32mpalíndromo\033[m.')
else:
    print(f'\nA frase {frase} invertida não gera a mesma frase ({inverso}), ou seja, '
          f'não é um \033[1:31mpalíndromo\033[m.')

