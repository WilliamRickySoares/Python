import matplotlib.pyplot as plt
import seaborn as sns


# Inicialização da lista de valores
valores = []


# Função para atualizar o gráfico
def atualizar_grafico():
    plt.clf()  # Limpa o gráfico anterior
    sns.lineplot(x = range(len(valores)), y = valores)  # Plota o gráfico de linha
    plt.pause(0.01)  # Breve pausa para exibir o gráfico atualizado


# Loop para adicionar valores à lista e atualizar o gráfico
while True:
    # Simulação de um novo valor sendo adicionado à lista
    novo_valor = float(input("Digite um novo valor (ou 'sair' para encerrar): "))

    valores.append(novo_valor)

    # Atualiza o gráfico
    atualizar_grafico()

# Exibe a lista completa de valores
print("Lista completa de valores:")
print(valores)

# Exibe o gráfico final
sns.lineplot(x = range(len(valores)), y = valores)
plt.show()
