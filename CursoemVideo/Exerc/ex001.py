user = input("Digite seu nome: ")
esp = str(' ')

msgPt = 'Olá Mundo! Começa agora o seu aprendizado em Python, {}!'
msgEN = 'Hello World! Begin now your learning in Python, {}!'

print(msgPt, user)
print(msgEN, user)
# Utilizar as chaves para ser substituida pela variáveil que vem depois
print('É um prazo em te conhecer, {}.'.format(user))

# Formas de fazer print e input na tela

print('')
print('# Contido na aula 07 modulo 1')
print('[Direita] Prazer em te conhecer: {:>20}!'.format(user))
print('[Esquerda] Prazer em te conhecer: {:<20}!'.format(user))
print('[Centralizado] Prazer em te conhecer: {:^20}!'.format(user))
print('[Central com Simbolos] Prazer em te conhecer: {:=^20}!'.format(user))
x = int(input('Quantas vezes o seu nome deve ser repetido? '))
print((user+' ') * x)
