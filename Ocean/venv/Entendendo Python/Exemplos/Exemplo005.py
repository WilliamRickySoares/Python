turma = []

while True:
    retorno = input("Digite: ")
    if retorno in 'Sair':
        break
    else:
        turma.append(retorno)
        
print(turma)