import pyodbc
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

start_time = datetime.now()
driver = "SQL Server"
server = 'SOARES'
data_base = 'middleware'

dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
print(dados_conexao)

conexao = pyodbc.connect(dados_conexao)
print("Conexão Bem Sucedida")
time2 = datetime.now()
print(f'Duração: {time2 - start_time}')

cursor = conexao.cursor()
cursor.execute("SELECT * FROM INFORMATION_SCHEMA.TABLES")
# Nome dos campos
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(num_fields)
print(field_names)

# Adiciona os valores às variáveis
myresult = cursor.fetchall()
for x in myresult:
    print(x)

time3 = datetime.now()
print(f'Duração: {time3 - time2}')

cursor.execute("SELECT codigo FROM Filiais")
num_fields = len(cursor.description)
field_names = [i[0] for i in cursor.description]
print(num_fields)
print(field_names)
myresult = cursor.fetchall()
for x in myresult:
    print(x[0])

time4 = datetime.now()
print(f'Duração: {time4 - time3}')

"""
# Conexao Banco de Dados
q = 0
while True:
    try:
        dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
        conexao = pyodbc.connect(dados_conexao)
        cursor = conexao.cursor()
    except:
        print(datetime.now())
        print("Tentando conectar novamente ao banco")
        q += 1
        if q >= quantidade_tentativas:
            print(datetime.now())
            print("Atingida quantidade de tentativas")
            break
    else:
        print(datetime.now())
        print("Conexão Realizada")
        break
    

"""