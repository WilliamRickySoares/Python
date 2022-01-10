# Desafio 005
# Faça um programa que leia um número inteiro e monstre na tela o seu sucessor e seu antecessor

print('# Desafio 005 '
      '\n# Faça um programa que leia um númeoro inteiro e monstre na tela o seu sucessor e seu antecessor')
n = int(input('\nDigite um número inteiro: '))
a = n-1
s = n+1

print('\nO digito escolhido foi {}, o seu antecessor é {} e seu sucessor é {}.'.format(n, a, s))
