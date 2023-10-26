
### Leia um numeros do usuario até ele digitar 0, e calcule a media dos numeros digitados.
lista = []
soma = contador = 0

while True:
    numero = float(input("Digite um número: "))
    contador += 1
    if numero != 0:
        lista.append(numero)
        contador += 1
    else:
        break
print(f"Foram adicionados {len(lista)} números, que somam {sum(lista)}!")
if contador == 1:
    print(f"O valor médio é o próprio número {sum(lista)}")
else:
    print(f"O valor médio é de {sum(lista) / len(lista)}")
print('FIM')




