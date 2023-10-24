# Problema 5
# Você está em um grupo de amigos e não consegue decidir onde almoçar hoje.
# Crie um programa que utilize a função random.choice() do módulo random para escolher aleatoriamente
# um restaurante da lista de opções de almoço.

import random
restaurantes = ['churrasco', 'oriental', 'pizzaria', 'sanduiche', 'peixaria']
print(f"Vamos comer hoje uma comida {random.choice(restaurantes)}!")
