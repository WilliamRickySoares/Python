print("""
Desafio 077 (M3A16)
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
""")

# Resultado do Curso em vídeo, Gustavo Guanabara
palavras = 'casa', 'boça', 'bola', 'feijao', 'arroz', 'teste', 'livre', 'arrojado'
for p in palavras:
    print(f'\nNa palavra \033[1:33m{p}\033[m temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

print('\n')
#  Meu resultado, utilizando uma lista onde o usúario preenche
vogais = 'a', 'e', 'i', 'o', 'u'
tupla = str(input(f'Digite: ')), str(input(f'Digite: ')), str(input(f'Digite: ')), str(input(f'Digite: '))
for n in tupla:
    print(f'\nNa palavra \033[1:33m{n}\033[m há as vogais:', end=' ')
    for i in range(len(n)):
        if n[i] in vogais:
            print(f'{n[i]}', end=' ')
print('\n')
