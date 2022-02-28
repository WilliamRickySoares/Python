# Estrutura "Condicional Aninhadas" pq tem uma condição dentro da outra

nome = str(input('Digite um nome: '))
if nome == 'William':
    print('Que nome bonito!')
elif nome in 'Maria João José Silva':
    print('Seu nome é bem comum no Brasil')
elif nome in 'Elisa Beatriz Erika Fernanda':
    print('Você tem o mesmo nome da minha filha')
elif nome in 'Silvia Valeria':
    print('Você tem o mesmo nome da minha esposa')
elif nome == 'Victor' or nome == 'Gabriel':
    print('Você tem o mesmo nome do meu filho')
else:
    print('Você tem um nome bem comum...')
print('Olá, tenha um bom dia, {}!'.format(nome.capitalize()))
