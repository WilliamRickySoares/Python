# Teórica
""" Aula 16 - Tuplas

Variáveis compostas (Tuplas)
    É uma variável que guarda vários valores / slot / dados

print(variavel[0]) # Mostra o elemento na posição 0, entre os colchetes
print(variavel[-4]) # Mostra o elemento na posição 4 contando do ultimo para o primeiro

for c in variavel: # Roda / Itera cada um dos elementos
    print(c) # Mostra cada um dos elemetos da variável

"As tuplas são IMUTÁVEIS"

Para criar uma tupla o conteudo da variável deve ser expressada entre parenteses.
Na versão nova, o parenteses é opcional.
"""

""" Prática """

# Tupla com parenteses
lanche1 = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche1)

# Tupla sem parenteses
lanche = 'Hamburguer', 'Suco', 'Pizza', 'Pudim'
print(lanche)
print(len(lanche))

print(lanche[0])  # Hamburquer, o primeiro
print(lanche[-2])  # Pizza, o penulitmo ou o segundo da direita pra esquerda
print(lanche[-2:])  # Da Pizza até o final


for comida in lanche:
    # print(comida)
    print(f'Eu comi {comida}')

for cont in range(0, len(lanche)):
    print(f'{lanche[cont]}')

for pos, cont in enumerate(lanche):
    print(f'Enumerate {cont} na posição {pos}')

a = (1, 2, 3, 5)
b = (7, 8, 10, 5)
c = a + b
print(c)
print(c.count(5))  # Count retorna a quantidade de vezes que o número aparece
print(c.index(8))  # Index retorna o número da posição do elemento

del lanche1  # A função 'del' apaga a variável


"""
Desafio 072
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte.

Seu programa deverá ler um numero pelo teclado (entre 0 e 20) e mostrá-lo
por extenso.

Desafio 073
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem da colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabetica;
d) Em que posição na tabela está o time da 'Chapecoense';

Desafio 074
Crie um programa que vai gerar cinco números aleatorios e colocar em um tupla.

Depois disso, mostre a listagem de números gerados e também indique o menor
e o maior valor que estão na tupla.

Desafio 075
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
a) Quantas vezes apareceu o valor 9.
b) Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares;

Desafio 076
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.

Desafio 077
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.



"""