# Exemplo 3
# Classifique a nota do aluno

nota = int(input("Insira a nota: "))
texto = "Classificação da nota foi de"

if nota > 8:
  print(texto, "A")
elif 8 <= nota > 6:
  print(texto, "B")
elif 6 <= nota > 4:
  print(texto, "C")
elif 4 < nota > 2:
  print(texto, "D")
elif nota <= 0:
  print(texto, "E")
else:
  print("Digite uma nota entre 0 e 10")
