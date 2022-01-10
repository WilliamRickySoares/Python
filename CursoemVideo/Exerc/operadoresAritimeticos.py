import math

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
pw = pow(n1, n2)
rest = n1 % n2
rq1 = float(math.sqrt(n1))
rq2 = float(math.sqrt(n2))
rq3 = float(n1**(1/2))
rq4 = float(n2**(1/2))
rc1 = float(n1**(1/3))
rc2 = float(n2**(1/3))

print('\nPara somar dois numeros utilize o sinal de [+] conforme >> {} + {} = {}'
      .format(n1, n2, soma))
print('Para subtrair dois numeros utilize o sinal de [-] conforme >> {} - {} = {}'
      .format(n1, n2, sub))
print('Para multiplicar dois numeros utilize o sinal de [*] conforme >> {} * {} = {}'
      .format(n1, n2, mul))
print('Para dividir dois numeros utilize o sinal de [/] conforme >> {} / {} = {:.2f}'
      .format(n1, n2, div))
print('Para elevar (exponênciação) utilize o sinal de [**] ou [pow(base,exp)] '
      'conforme >> {} ** {} = {} ou pow({},{}) = {}'
      .format(n1, n2, exp, n1, n2, pw))
print('Para dividir e mostrar somente a parte inteira utilize o sinal de [//] conforme >> {} // {} = {}'
      .format(n1, n2, dint))
print('Para mostrar o resto de uma divisão utilize o sinal de [%] conforme >> {} % {} = {}'
      .format(n1, n2, rest))
print('Para mostrar a raiz quadrada utilize [math.scrt()] conforme >> math.scrt({}) = {:.6f} | math.scrt({}) = {:.6f}'
      .format(n1, rq1, n2, rq2))
print('Para mostrar a raiz quadrada de OUTRA forma utilize [**(1/2)] depois do valor / variável '
      'conforme >> {} ** (1/2) = {:.6f} | {} ** (1/2) = {:.6f}'
      .format(n1, rq3, n2, rq4))
print('Para mostrar a raiz cúbica utilize [**(1/3)] depois do valor / variável '
      'conforme >> {} ** (1/3) = {:.6f} | {} ** (1/c) = {:.6f}'
      .format(n1, rc1, n2, rc2))

print('\n# Ordem de precedencia: \n1º   ()\n2º   ** \n3º   *   /   //   %\n4º   +   -')
