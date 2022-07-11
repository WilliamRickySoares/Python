"""
# Aula 13
Laços, iteração, Loop e for

"""

'''
laco c no intervalo(1,10)
    passo
pega

'''

# progressivo
print('\nProgressivo')
for c in range(1, 5):
    print(c)

# regressivo
print('\nRegressivo')
for c in range(5, 1, -1):
    print(c)

# For customizável
i = int(input('\nQual o número inicial da contagem: '))
f = int(input('Qual o numero final da contagem: '))
p = int(input('De quantos em quantos números devem ser contados: '))

for c in range(i, f+1, p):
    print(c)

# Somando no for
print('\n Somando no for')
s = 0
for c in range(1, 5):
    n = int(input('Digite um número: '))
    s += n
print(f'A soma no laço é de {s}')

