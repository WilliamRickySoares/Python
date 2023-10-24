# Exercicio 2

# Carro flex
#
# ## se o valor etanol for maior que 70% do valor do valor gasolina -> gasolina
# ## se o valor do etanol for menor ou igual a 70% do valor gasolina -> etanol
#
# #gasolina, etanol = 4, 1
# etanol#gasolina, etanol = 4, 3
# gasolina#gasolina, etanol = 10, 7
# etanol#gasolina, etanol = 10, 7.0000000001
# #gasolina

valor_gasolina = float(input(f"Valor da gasolina: "))
valor_etanol = float(input("Valor do etanol: "))
comparacao = valor_etanol / valor_gasolina
print(f"A diferença dos preços entre gasolina e etanol é de {(comparacao*100):.2f}%. Então, ", end="")
if comparacao > 0.7:
    print(f"é recomendável abastecer com \033[1;30;41mGASOLINA\033[m!")
else:
    print(f"é recomendável abastecer com \033[1;30;41mETANOL\033[m!")
