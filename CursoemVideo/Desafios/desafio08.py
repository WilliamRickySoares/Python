# Desafio 008
# Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros

print('# Desafio 008 '
      '\n# Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros')

m = float(input('\nDigite o valor em metros >>> '))

print('\nO valor em metros digitado foi {}, e equivale a: {} (dm) decametros, {} (km) kilometros'
      ', {:.0f} (cm) centimetros, {:.0f} (mm) milimetros'
      .format(m, (m/10), (m/1000), m*100, m*1000))
