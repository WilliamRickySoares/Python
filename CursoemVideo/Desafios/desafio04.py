print(' ### Execercio 4 ###')
print(' ### Identificar que tipos o que foi digitado é ou não ###')

print('')
nAlg = input('Digite algo para identificarmos: ')
print('Você digitou "{}"'.format(nAlg))
print('')
print('O tipo primitivo é {}'.format(type(nAlg)))
print('É um número? {}'.format(nAlg.isnumeric()))
print('Está em maiucula? {}'.format(nAlg.isupper()))
print('É alfanumerico? {}'.format(nAlg.isalnum()))
print('É alfabético? {}'.format(nAlg.isalpha()))
print('Está em ASCII? {}'.format(nAlg.isascii()))
print('É um número decimal? {}'.format(nAlg.isdecimal()))
print('É um digito? {}'.format(nAlg.isdigit()))
print('É um indentificador? {}'.format(nAlg.isidentifier()))
print('Está em minusculo? {}'.format(nAlg.islower()))
print('É imprimível? {}'.format(nAlg.isprintable()))
print('São espações? {}'.format(nAlg.isspace()))
print('É um título? {}'.format(nAlg.istitle()))
