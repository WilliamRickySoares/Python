import pyaudio
import math
import matplotlib.pyplot as plt
import time


# Listas para armazenar os valores
lista = []
valores = []
qtd_valores = 150


def calculate_db(data1):
    rms = math.sqrt(sum([sample**2 for sample in data1]) / len(data1))
    db1 = 20 * math.log10(rms)
    return db1


# Função para atualizar o gráfico
def atualizar_grafico():
    # Limpa a figura anterior
    plt.clf()

    # Plota a linha com os valores atualizados
    plt.plot(valores)

    # Mostra o gráfico atualizado
    plt.draw()
    plt.pause(0.001)


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

print("Medindo decibéis. Pressione Ctrl+C para sair.")

try:
    while True:
        data = stream.read(CHUNK)
        data = [int.from_bytes(data[i:i+2], byteorder='little', signed=True) for i in range(0, len(data), 2)]
        db = calculate_db(data)
        try:
            valor = float(db)

            # Adiciona o novo valor à lista
            lista.append(valor)
            if len(lista) > qtd_valores:
                valores = lista[-qtd_valores:]
            else:
                valores = lista

            # print(valores)

            # Atualiza o gráfico
            atualizar_grafico()
            time.sleep(0.3)

        # Exibe o gráfico final e a lista completa de valores
        except ValueError:
            print("Valor inválido. Tente novamente.")
        # print(f"Decibéis: {valor} dB")


except KeyboardInterrupt:
    pass

plt.plot(valores)
plt.show()
stream.stop_stream()
stream.close()
p.terminate()
