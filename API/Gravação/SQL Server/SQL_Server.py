import pyodbc
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

driver = "SQL Server"
server = 'SOARES'
data_base = 'middleware'

dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
print(dados_conexao)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")
