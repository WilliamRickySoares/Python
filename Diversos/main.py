import pyaudio
import math


def calculate_db(data):
    rms = math.sqrt(sum([sample**2 for sample in data]) / len(data))
    db = 20 * math.log10(rms)
    return db

def main():
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
            print(f"Decibéis: {db} dB")

    except KeyboardInterrupt:
        pass

    stream.stop_stream()
    stream.close()
    p.terminate()

if __name__ == '__main__':
    main()
