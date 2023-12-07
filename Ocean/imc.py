"""
IMC	Classificação
Menor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III
"""

peso = float(input("Insera o seu peso: "))
altura = float(input("Insera o seu altura: "))
imc = peso / (altura ** 2)
print(f"Seu imc é de {imc:.2f}")

classificacao = ""
if imc > 40:
    classificacao = "Obesidade grau III"
elif 40 > imc >= 35:
    classificacao = "Obesidade grau II"
elif 35 > imc >= 30:
    classificacao = "Obesidade grau I"
elif 30 > imc >= 25:
    classificacao = "Sobrepeso"
elif 25 > imc >= 18.5:
    classificacao = "Normal"
elif imc < 18.5:
    "Magreza"

print(f"Sua classificação é de {classificacao}")

