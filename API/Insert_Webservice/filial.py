import requests
import xmltodict
import pyodbc
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

# Variaveis
driver = "SQL Server"
server = 'SOARES'
data_base = 'middleware'
base = "Total"
user = "WebService"
senha = "Fusion_100%$"
print("Variáveis definidas")

# Conexao Banco de Dados
dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
print("Conexão Bem Sucedida")

link = "http://maxservrr.ddns.net:8181/RadarWebWebServices/"

# Post Filial
link_post = link + 'Areas/Empresarial/Empresarial.svc/json/BuscarFiliais'
str_json = {
    "login": {
        "Base": base,
        "Usuario": user,
        "Senha": senha
    },
    "filtro": {
        "IncluirFiliaisInativas": True
    }
}

# Estruturação
dados_request = requests.post(link_post, json = str_json)
dados_parse = xmltodict.parse(dados_request.content)
print("Estruturação dos dados")

qtd_registro_webservice = len(dados_parse['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'])
print(f'Qtd de campos de Filiais cadastrados na webservice: {qtd_registro_webservice}')

linhas_registros = 0
while True:
    Codigo = int(dados_parse['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros]['a:Codigo'])
    Nome = dados_parse['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros]['a:Nome']
    NomeFantasia = dados_parse['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros]['a:NomeFantasia']

    str_consulta = f"select Codigo from Filiais where Codigo = {Codigo}"
    str_update = f"update Filiais set Nome = '{Nome}', NomeFantasia = '{NomeFantasia}', AdicionadoEm = '{datetime.now()}' where Codigo = {Codigo}"
    str_insert = f"insert into Filiais (Codigo, Nome, NomeFantasia, AdicionadoEm) values ('{Codigo}', '{Nome}', '{NomeFantasia}', '{datetime.now()}')"

    exec_consulta = cursor.execute(str_consulta)
    print(f'\n{str_consulta}')
    try:
        key = cursor.fetchone()[0]
        exec_update = cursor.execute(str_update)
        cursor.commit()
        print(str_update)
    except TypeError:
        exec_insert = cursor.execute(str_insert)
        cursor.commit()
        print(str_insert)

    linhas_registros += 1

    if linhas_registros >= qtd_registro_webservice:
        print("Fim da lista")
        break
