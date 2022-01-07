print('### Curso Python #07')
print('### 05/01/20222')
print('')

print('# Operadores Aritméticos')
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))

# Os cálculos com os operadores aritimeticos deve ser feito da forma abaixo
soma = n1 + n2
sub = n1 - n2
mul = n1 * n2
div = n1 / n2
dint = n1 // n2
exp = n1 ** n2
rest = n1 % n2

print('Para somar dois numeros utilize o sinal de [+] conforme >> {} + {} = {}'
      .format(n1, n2, soma))
print('Para subtrair dois numeros utilize o sinal de [-] conforme >> {} - {} = {}'
      .format(n1, n2, sub))
print('Para multiplicar dois numeros utilize o sinal de [*] conforme >> {} * {} = {}'
      .format(n1, n2, mul))
print('Para dividir dois numeros utilize o sinal de [/] conforme >> {} / {} = {:.2f}'
      .format(n1, n2, div))
print('Para elevar (exponênciação) utilize o sinal de [**] conforme >> {} ** {} = {}'
      .format(n1, n2, exp))
print('Para dividir e mostrar somente a parte inteira utilize o sinal de [//] conforme >> {} // {} = {}'
      .format(n1, n2, dint))
print('Para mostrar o resto de uma divisão utilize o sinal de [%] conforme >> {} % {} = {}'
      .format(n1, n2, rest))
print('')

print('# Ordem de precedencia: \n1º   ()\n2º   ** \n3º   *   /   //   %\n4º   +   -')
