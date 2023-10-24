# Exemplo 2
# Identifique se um número é impar ou par

valor = int(input("Digite um número para idefitifcar se é impar ou par: "))

calculo = valor % 2

if calculo == 0:
  print(f"{valor} é par")
else:
  print(f"{valor} é impar")
