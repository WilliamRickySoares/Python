import pyodbc
import time
import credential

def conectar():
    driver = "SQL Server"
    server = credential.server_base
    data_base = credential.data_base
    dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
    quantidade_tentativas = 5  # Quantidade de tentativa de conexão ao banco de dados
    tentativas_realizadas = 1

    while True:
        try:
            print("Conectando ao banco...")
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            print("Conexão com o banco realizada!\n")
            break
        except pyodbc.OperationalError:
            print("Error conexão")
            print("Tentando novamente...")
            time.sleep(2)
            print(f"Nova Tentativa {tentativas_realizadas}")
            tentativas_realizadas += 1
            if tentativas_realizadas == quantidade_tentativas:
                break
    return cursor
