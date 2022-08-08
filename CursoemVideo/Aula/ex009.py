# Conjunto de dicas para trabalhar com textos. Aula #09

frase = 'Curso em Video Python'
print(frase)
print('\nA frase um total de {} caracteres.'.format(len(frase)))
print('O caracter 3 da frase = "{}".'.format(frase[3]))
print('O trecho do caracter 9 ao caracter 14 = "{}".'.format(frase[9:14]))
print('O trecho a partir do caracter 15 em diante = "{}".'.format(frase[15:]))
print('O trecho até o até o caracter 14 = "{}".'.format(frase[:14]))
print('Pegar um trecho e pular de 2 em 2 = "{}"'.format(frase[1:15:2]))
print('Pegar toda a frase pular de 3 em 3 = "{}"'.format(frase[::3]))
print('Contar a quantidade de vezes que um caracter aparece. Na frase tem = {} "o".'.format(frase.count('o')))
print('Tornar a frase maiuscula = "{}"'.format(frase.upper()))
print('Tornar a frase minuscula = "{}"'.format(frase.lower()))
print('Localizar a posição do caracter = {}'.format(frase.find('o')))
print('Substituir na visualização "Python" por "Android" = "{}"'.format(frase.replace('Python', 'Android')))
print('O trecho "Curso" esta na frase? {}'.format('Curso' in frase))

print('\n****************************\n')
nome = 'José'
idade = 33
salario = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salario:.2f}')
print(f'Esse nome {nome:20} é lindo') #20 espaços
print(f'Esse nome {nome:^20} é lindo') #20 espaços centralizado
print(f'Esse nome {nome:-^20} é lindo') #20 espaços centralizado com traço
print(f'Esse nome {nome:-<20} é lindo') #alinhado a esquerda
print(f'Esse nome {nome:->20} é lindo') #alinhado a direita

print('\n****************************\n')

print('\nBloco de textos\n')
print('''"Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod t
empor incididunt ut labore et dolore magna 
aliqua. Ut enim ad minim veniam, 
quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. 
Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat 
non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."\n''')

print('Procurar depois de colocar tudo em minusculo = {}'.format(frase.lower().find('video')))
print('Frase separada por cada espaço "{}"'.format(frase.split()))
print('Depois de fazer o split da frase, ela se torna uma lista. '
      'Podemos atribuir o resultado e chamar somente um dos itens da lista')

print("""
Transformação
frase.replace(‘Python’, ‘Android’) » vai substituir Python por Android

frase.upper() » coloca toda a frase em maiúsculo.

frase.lower() » coloca toda a frase em minúsculo.

frase.capitalize() » deixa somente a primeira letra da string em maiúsculo.

frase.title() » deixa a primeira letra de todas as palavras em maiúsculo.

frase.strip() » elimina todos os espaços no início e no fim.

frase.rstrip() » elimina todos os espaços da direita.

frase.lstrip() » elimina todos os espaços da esquerda.

Divisão
frase.split() » cria uma divisão onde na string onde tem espaço. E cada separação é recomeçada a contagem. Cria uma lista.

Junção
‘-‘.join(frase) » junta os elemento de frase usando como separador o – .

Usando dois comandos
frase.lower().find(‘video’)

Tirar os espaços de uma string
c = frase.split()
frasejunta = ”.join(c)

Inverso de uma string
frase[::-1]

""")