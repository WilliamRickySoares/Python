print("""
Desafio 064
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números
foram digitados e qual foi a soma entre eles
(desconsiderando o flag)
""")

c = r = 0
n = int(input('Digite um número: '))
while n != 999:
    r += n
    c += 1
    n = int(input('Digite um número: '))

print(f'\nE foram digitados \033[1:33m{c}\033[m números.')
print(f'A soma dos números é \033[1:33m{r}\033[m.')
