# TODO: Incompleto

# Exercicio 1

# Equação de 2 Grau# ax² + bx + c = 0
# x² - x + 1 = 0 -> delta = -3 < 0
# x² +2x + 1 = 0 -> delta = 0
# x^2 - 4x = 0 - > delta = 16 > 0

print("Equação quadrática ou Equação de segundo grau")
print("ax² + bx + c = 0")

valor_a = float(input("Digite o valor de 'a': "))
valor_b = float(input("Digite o valor de 'b': "))
valor_c = float(input("Digite o valor de 'c': "))

delta = (valor_b ** 2) - 4 * valor_b * valor_c
print(f"Delta = {delta}")
valor_x = - valor_b + delta ** (1/2) / 2 * valor_a

print(f"x é igual a {valor_x}")

