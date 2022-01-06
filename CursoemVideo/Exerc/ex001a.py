# exercício da aula #06 Curso Python #06 - Tipos Primitivos e Saída de Dados

n1 = int(input('Digite o número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma vale', s)
print('A soma entre', n1, 'e', n2, 'é igual a', s)  # Jeito menos inteligente de concatenar

print('A soma entre {} e {} é igual a {}'.format(n1, n2, s))

# int() para inteiros. Exemplo: 7 -4 0 9875
# float() para fracionados. Exemplo: 4.5 0.076 -15.223 7.0
# bool() para boolanos. Exemplo: True, False (com a inicial maiuscula)
# str() para string | texto. Exemplo: 'Olá', '7.5', ''

n1 = int(input('Digite um valor: '))
print(type(n1))

n2 = input('Digite algo: ')
print(n2.isnumeric())

n3 = input('Digite uma letra: ')
print(n3.isupper())