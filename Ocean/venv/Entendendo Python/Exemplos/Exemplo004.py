## Exercicio Conversão de Celsius para Fahrenheit
## C * 9/5  + 32 = F
print('''
# C = 0;   F = 32
# C = 100; F = 212
# C = -10; F = 14
''')

c = int(input("Digite o valor em Celsus: "))

f = c * 9 / 5 + 32

print(f"O valor de {c:.2f} Cº (Celsus) equivale à {f:.2f} Fº (Fahrenheit)")