print("""
Desafio 067
Faça um programa que mostre a tabuada de vários números, um de cada vez, 
para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.
""")

t = 0
while True:
    n = int(input('\nQual o número da tabuada: '))
    if n <= 0:
        break
    while True:
        t += 1
        m = n * t
        print(f'{t} * {n} = {m}')
        if t >= 10:
            t = 0
            break
print(f'Tabuada encerrada!')
