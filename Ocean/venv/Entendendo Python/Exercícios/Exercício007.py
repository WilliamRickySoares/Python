# Problema 4
# Escreva um programa que solicite ao usuário um número inteiro positivo e, em seguida,
# faça uma contagem regressiva a partir desse número até zero, imprimindo cada número no processo.

numero = int(input("Digite um número inteiro: "))
while numero >= 0:
    print(numero)
    numero -= 1
