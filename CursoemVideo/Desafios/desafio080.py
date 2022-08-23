print("""Desafio 080
Crie um programa onde o usuário possa digitar cinco valores numéricos e
cadastre-os em uma lista, já na posição correta da inserção 
(sem usar o sort()). No final, mostre a lista ordenada na tela.
""")
# TODO: Resposta copiada do vídeo, não realizada previamente.

lista = list()

for i in range(0, 5):
    n = int(input('Adicione um número à lista: '))
    if i == 0 or n > max(lista):
        lista.append(n)
        print(f'Número {n} adicionado a lista!')
        # print(f'Lista > {lista}')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Número {n} inserido na posição {pos}')
                # print(f'Lista > {lista}')
                break
            pos += 1

print(f'Lista > {lista}')
