# Exemplo 1
# Contruir um programa em que o usuário informa uma nota e esta é classificada nos graus A, B, C, D e E

while True:
  try:
    nota = int(input("Insira a nota: "))
    texto = "Classificação da nota foi de"
    if nota > 7 and nota <= 10:
      print(texto, "A")
    elif nota <= 7 and nota > 5:
      print(texto, "B")
    elif nota <= 5 and nota > 3:
      print(texto, "C")
    elif nota <= 3 and nota > 0:
      print(texto, "D")
    elif nota <= 0:
      print(texto, "E")
    else:
      print("Digite uma nota entre 0 e 10")
    break
  except:
    print("Favor verificar o valor digitado, use somente números")
