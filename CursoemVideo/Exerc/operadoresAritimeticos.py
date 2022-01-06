print('### Curso Python #07')
print('### 05/01/20222')
print('')

print('# Operadores Aritméticos')
n1 = int(5)
n2 = int(2)
print('Para somar dois numeros utilize o sinal de [+] conforme >> {} + {} = {}'
      .format(n1, n2, (n1+n2)))
print('Para subtrair dois numeros utilize o sinal de [-] conforme >> {} - {} = {}'
      .format(n1, n2, (n1-n2)))
print('Para multiplicar dois numeros utilize o sinal de [*] conforme >> {} * {} = {}'
      .format(n1, n2, (n1*n2)))
print('Para dividir dois numeros utilize o sinal de [/] conforme >> {} / {} = {}'
      .format(n1, n2, (n1/n2)))
print('Para elevar (exponênciação) utilize o sinal de [**] conforme >> {} ** {} = {}'
      .format(n1, n2, (n1**n2)))
print('Para dividir e mostrar somente a parte inteira utilize o sinal de [//] conforme >> {} // {} = {}'
      .format(n1, n2, (n1//n2)))
print('Para mostrar o resto de uma divisão utilize o sinal de [%] conforme >> {} % {} = {}'
      .format(n1, n2, (n1 % n2)))
print('')

print('# Ordem de precedencia:')
print('1º   () ')
print('2º   ** ')
print('3º   *   /   //   % ')
print('4º   +   -')
