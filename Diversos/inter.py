import matplotlib.pyplot as plt

# Lista inicial vazia para armazenar os valores
valores = []


# Função para atualizar o gráfico
def atualizar_grafico():
    # Limpa a figura anterior
    plt.clf()

    # Plota a linha com os valores atualizados
    plt.plot(valores)

    # Mostra o gráfico atualizado
    plt.draw()
    plt.pause(0.001)


# Loop para adicionar valores à lista
while True:
    novo_valor = float(input("Digite um valor (ou 'sair' para sair): "))
    if novo_valor == 'sair':
        break

    # Adiciona o novo valor à lista
    valores.append(novo_valor)

    # Atualiza o gráfico
    atualizar_grafico()

# Exibe o gráfico final e a lista completa de valores
plt.plot(valores)
plt.show()

# Imprime a lista completa de valores
print("Lista completa de valores:", valores)
