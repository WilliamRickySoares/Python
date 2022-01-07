# Trbalhando com print
# O [end=''] permite que o print seguinte fique na mesma linha do print atual
# O [\n] insere uma quebra de linha

user = input("Digite seu nome >>> ")
x = int(input('Quantas vezes o seu nome deve ser repetido? >>> '))

# Concatenar dois textos da forma antiga
msgPt = '\nOlá Mundo! Começa agora o seu aprendizado em Python, '
print(msgPt, user)

# Concatenar dois textos de forma inteligente
print('Hello World! Begin now your learning in Python, {}!'.format(user))

# Utilizar as chaves para ser substituida pela variáveil que vem depois
print('\nÉ um prazo em te conhecer, {}.'.format(user))
print('Nice to meet you, {}.'.format(user))

# Formas de organizar o texto da variável dentro da frase
print('\n# Contido na aula 07 modulo 1')
print('[Direita] Prazer em te conhecer: {:>{}}!'.format(user, x))
print('[Esquerda] Prazer em te conhecer: {:<20}!'.format(user))
print('[Centralizado] Prazer em te conhecer: {:^20}!'.format(user))
# noinspection PyStringFormatqa
print('[Central com Simbolos] Prazer em te conhecer: {:=^20}!'.format(user))

# Repetindo um texo uma quantidade especifica de vezes
xUser = (user+' ') * x
print(xUser)
print('{}'.format(xUser))
