import pyodbc

server = '127.0.0.1,1433'
database = 'fusionMaxserv'
database_middlware = 'middleware'
username = 'sa'
password = 'neo@123'

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

conn_middleware = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database_middlware+';UID='+username+';PWD='+ password)
cursor_middleware = conn_middleware.cursor()

# Leitura de Tabelas do Middlware
ler_tabelas = """SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES"""
ler_filiais = """SELECT * FROM [Filiais]"""
ler_cliente = """SELECT * FROM [Clientes]"""
ler_condpgto = """SELECT * FROM [CondicaoPagamentos]"""
ler_formapagamento = """SELECT * FROM [FormaPagamentos]"""
ler_infopluscomplementar = """SELECT * FROM [InfoPlusComplementares]"""
ler_infoplus = """SELECT * FROM [InfoPluss]"""
ler_itemtabelapreco = """SELECT * FROM [ItemTabelaPrecos]"""
ler_servico = """SELECT * FROM [Servicoss]"""
ler_tabelapreco = """SELECT * FROM [TabelaPrecos]"""
ler_tipocobranca = """SELECT * FROM [TipoCobrancass]"""
ler_tipocob = """SELECT * FROM [TipoCobs]"""

# Leitura de Tabelas do Fusion
ler_acompanhamento = """SELECT * FROM [D_formArkoTotalAcompanhamento] 
    where 1=1 and wfprocess_neoId is not null order by neoid desc """
ler_cadastro = """SELECT * FROM [D_formArkoTotalCadAcompanhamento] where txSeqTicketCad = '000443'"""

cursor.execute(ler_cadastro)
cursor_middleware.execute(ler_filiais)

for linha in cursor:
    print(linha)

for linha in cursor_middleware:
    print(linha)

print(len("11.123.123/1231-12"))
