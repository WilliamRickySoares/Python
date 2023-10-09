import pyodbc
import time
import credential
from loguru import logger


def conectar():
    driver = "SQL Server"
    server = credential.server_base
    data_base = credential.data_base
    dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
    quantidade_tentativas = 5  # Quantidade de tentativa de conexão ao banco de dados
    tentativas_realizadas = 1

    while True:
        try:
            logger.info("Conectando ao banco...")
            conexao = pyodbc.connect(dados_conexao)
            cursor = conexao.cursor()
            logger.info("Conexão com o banco realizada!\n")
            break
        except pyodbc.OperationalError:
            logger.warning("Error conexão")
            logger.info("Tentando novamente...")
            time.sleep(2)
            logger.warning(f"Nova Tentativa {tentativas_realizadas}")
            tentativas_realizadas += 1
            if tentativas_realizadas == quantidade_tentativas:
                logger.error("Interrompendo a tentativa de conexão ao banco")
                break
    return cursor
