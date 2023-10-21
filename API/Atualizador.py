import requests
import xmltodict
import pyodbc
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)

horario_inicio = datetime.now()
print(horario_inicio)

# Variaveis
driver = "SQL Server"
server = 'SOARES'
data_base = 'middleware'
quantidade_tentativas = 5  # Quantidade de tentativa de conexão ao banco de dados

# Dados de acesso ambiente de teste da WK
# base = "demo"
# user = "wk"
# senha = "wk"

# Dados de acesso ao ambiente de produção da Maxserv
base = "TOTAL"
user = "FUSION"
senha = "GsiTNjR*@LuoL3"

# link = "http://maxservrr.ddns.net:9091/RadarWebService/"
link = "http://totalmaxserv.ddns.net:9091/RadarWebWebServices/"

# """Conexao Banco de Dados"""
print("Conectando ao banco...")
dados_conexao = f"Driver={driver};Server={server};Database={data_base};"
conexao = pyodbc.connect(dados_conexao)
cursor = conexao.cursor()
print("Conexão com o banco realizada!")

def enumInfoPlus(info):
    retorno_tipo_infoplus = ''
    if info == 'Data_DDMMAAAA':
        retorno_tipo_infoplus = 0
    if info == 'Data_MMAAAA':
        retorno_tipo_infoplus = 1
    if info == 'Alfanumerico':
        retorno_tipo_infoplus = 2
    if info == 'Numerico':
        retorno_tipo_infoplus = 3
    if info == 'ValorV2':
        retorno_tipo_infoplus = 4
    if info == 'ValorV4':
        retorno_tipo_infoplus = 5
    if info == 'ValorV8':
        retorno_tipo_infoplus = 6
    if info == 'InformacoesComplementares':
        retorno_tipo_infoplus = 7
    if info == 'HoraHHMM':
        retorno_tipo_infoplus = 8
    if info == 'CheckBox':
        retorno_tipo_infoplus = 9
    return retorno_tipo_infoplus

def atualizadorFilial():
    # Post Filial
    link_post_filial = link + 'Areas/Empresarial/Empresarial.svc/json/BuscarFiliais'
    print(f'Buscar dados utilizando a URL: {link_post_filial}')
    str_json_filial = {
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
    dados_request_filial = requests.post(link_post_filial, json = str_json_filial)
    print(f'dados_request = {dados_request_filial}')
    dados_parse_filial = xmltodict.parse(dados_request_filial.content)
    print(datetime.now())
    print("Dados estruturados")

    qtd_registro_webservice_filial = len(dados_parse_filial['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'])
    print(f'Qtd de campos de Filiais cadastrados na webservice: {qtd_registro_webservice_filial}')

    linhas_registros = 0
    while True:
        Codigo_filial = int(dados_parse_filial['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros]['a:Codigo'])
        Nome_filial = dados_parse_filial['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros]['a:Nome']
        NomeFantasia_filial = dados_parse_filial['BuscarFiliaisResponse']['BuscarFiliaisResult']['a:Filial'][linhas_registros][
            'a:NomeFantasia_filial']

        str_consulta_filial = f"select [Codigo] from [Filiais] where [Codigo] = {Codigo_filial}"
        str_update_filial = f"update [Filiais] set [Nome] = '{Nome_filial}', [NomeFantasia_filial] = '{NomeFantasia_filial}', [AdicionadoEm] = '{datetime.now()}' where [Codigo] = {Codigo_filial}"
        str_insert_filial = f"insert into [Filiais] ([Codigo], [Nome], [NomeFantasia_filial], [AdicionadoEm]) values ('{Codigo_filial}', '{Nome_filial}', '{NomeFantasia_filial}', '{datetime.now()}')"

        print(datetime.now())
        exec_consulta = cursor.execute(str_consulta_filial)
        print(f'\n{str_consulta_filial}')
        try:
            key = cursor.fetchone()[0]
            exec_update = cursor.execute(str_update_filial)
            cursor.commit()
            print(str_update_filial)
        except TypeError:
            exec_insert = cursor.execute(str_insert_filial)
            cursor.commit()
            print(str_insert_filial)

        linhas_registros += 1

        i = linhas_registros
        registros = i
        if registros >= qtd_registro_webservice_filial:
            print(datetime.now())
            print("Fim da lista")
            break

def atualizadorCliente():
    # Post Cliente
    link_post_cliente = link + 'Areas/Empresarial/Empresarial.svc/json/LerCFRTs'
    print(f'Buscar dados utilizando a URL: {link_post_cliente}')
    str_json_cliente = {
        "login": {
            "Base": base,
            "Usuario": user,
            "Senha": senha
        },
        "filtro": {
            "TipoPessoa": 0,
            "SituacaoCFRT": 0,
            "TipoCFRT": 67,
            "BuscarDadosInfoPlus": True
        }
    }

    # Estruturação
    dados_request_cliente = requests.post(link_post_cliente, json = str_json_cliente)
    print(f'dados_request = {dados_request_cliente}') # Status da conexão, se 200 OK
    dados_parse_cliente = xmltodict.parse(dados_request_cliente.content)

    qtd_registro_webservice_cliente = len(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'])
    print(f'Qtd de campos de Filiais cadastrados na webservice: {qtd_registro_webservice_cliente}')

    # linhas_registros = 0
    for linhas_registros in range(0, (qtd_registro_webservice_cliente) ):
        Codigo_Cliente = int(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:Codigo'])
        Classificacao_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:Classificacao'])
        RazaoSocial_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:RazaoSocial'])
        if "@i:nil" in RazaoSocial_cliente:
            RazaoSocial_cliente = 'NULL'

        NomeFantasia_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:NomeFantasia'])
        if "@i:nil" in NomeFantasia_cliente:
            NomeFantasia_cliente = 'NULL'

        CodigoCondicaoPagamento_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:CodigoCondicaoPagamento'])
        if CodigoCondicaoPagamento_cliente == 'None':
            CodigoCondicaoPagamento_cliente = 'NULL'

        CodigoFormaPagamento_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:CodigoFormaPagamento'])
        if CodigoFormaPagamento_cliente == 'None':
            CodigoFormaPagamento_cliente = 'NULL'

        CodigoTabelaPrecoServico_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:CodigoTabelaPrecoServico'])
        if CodigoTabelaPrecoServico_cliente == 'None':
            CodigoTabelaPrecoServico_cliente = 'NULL'

        CPF_CNPJ_cliente = str(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:CPF_CNPJ'])
        if CPF_CNPJ_cliente == 'None':
            CPF_CNPJ_cliente = 'NULL'

        # TipoCobranca = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:TipoCobranca']['a:Codigo']

        # TipoCobranca
        # Codigo
        # Descricao


        str_consulta_cliente = f"select [Codigo] from [Clientes] where [Codigo] = {Codigo_Cliente};"
        str_update_cliente = f"update [Clientes] set [Classificacao] = '{Classificacao_cliente}', [RazaoSocial] = '{RazaoSocial_cliente}', [NomeFantasia] = '{NomeFantasia_cliente}', [CodigoCondicaoPagamento] = '{CodigoCondicaoPagamento_cliente}', [CodigoTabelaPrecoServico] = '{CodigoTabelaPrecoServico_cliente}', [AdicionadoEm] = '{datetime.now()}', [CPF_CNPJ] = '{CPF_CNPJ_cliente}', [Cortesia] = 0 where [Codigo] = {Codigo_Cliente};"
        # , TipoCobCodigo = {TipoCobranca},
        str_insert_cliente = f"insert into [Clientes] ([Codigo], [Classificacao], [RazaoSocial], [NomeFantasia], [CodigoCondicaoPagamento], [CodigoTabelaPrecoServico], [AdicionadoEm], [CPF_CNPJ], [Cortesia]) values ('{Codigo_Cliente}', '{Classificacao_cliente}', '{RazaoSocial_cliente}', '{NomeFantasia_cliente}', '{CodigoCondicaoPagamento_cliente}', '{CodigoTabelaPrecoServico_cliente}', '{datetime.now()}', '{CPF_CNPJ_cliente}', 0);"
        #  {TipoCobranca}

        exec_consulta = cursor.execute(str_consulta_cliente)
        try:
            # print(str_update_cliente)
            key = cursor.fetchone()[0]
            exec_update = cursor.execute(str_update_cliente)
            cursor.commit()
            print(f'{Codigo_Cliente} Atualizado')
        except TypeError:
            # print(str_insert_cliente)
            exec_insert = cursor.execute(str_insert_cliente)
            cursor.commit()
            print(f'{Codigo_Cliente} Adicionado')


        qtd_info_inseridos = 0
        qtd_info_plus = len(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos])
        while True:
            # print(dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'])
            InfoPlus_Descricao = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:Descricao']
            InfoPlus_Grupo = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:Grupo']
            InfoPlus_IdHeader = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:IdHeader']
            InfoPlus_Obrigatorio = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:Obrigatorio']
            InfoPlus_TipoInfoPlus_temp = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:TipoInfoPlus']
            InfoPlus_TipoInfoPlus = enumInfoPlus(InfoPlus_TipoInfoPlus_temp)
            InfoPlus_Valor = dados_parse_cliente['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'][linhas_registros]['a:DadosInfoPlus']['a:InfoPlus'][qtd_info_inseridos]['a:Valor']
            """
            select * from [InfoPluss] where [Descricao] = '' and [Grupo] = '' and [IdHeader] = '' and [ClienteCodigo] = '';
            update [InfoPluss] set [Valor] = '', [AdicionadoEm] = '' where [Descricao] = '' and [Grupo] = '' and [IdHeader] = '' and [ClienteCodigo] = '';
            insert into InfoPluss ([Descricao], [Grupo], [IdHeader], [Obrigatorio], [TipoInfo], [Valor], [AdicionadoEm], [ClienteCodigo]) values ('Desc', 'G', 'He', 'Ob', 'Tipo', 'Va', 'Add', 'Cli');
            """

            str_consulta_cliente_infoplus = f"select * from [InfoPluss] where [Descricao] = '{InfoPlus_Descricao}' and [Grupo] = '{InfoPlus_Grupo}' and [IdHeader] = '{InfoPlus_IdHeader}' and [ClienteCodigo] = '{Codigo_Cliente}';"
            str_update_cliente_infoplus = f"update [InfoPluss] set [Valor] = '{InfoPlus_Valor}', [AdicionadoEm] = '{datetime.now()}' where [Descricao] = '{InfoPlus_Descricao}' and [Grupo] = '{InfoPlus_Grupo}' and [IdHeader] = '{InfoPlus_IdHeader}' and [ClienteCodigo] = '{Codigo_Cliente}';"
            str_insert_cliente_infoplus = f"insert into [InfoPluss] ([Descricao], [Grupo], [IdHeader], [Obrigatorio], [TipoInfo], [Valor], [AdicionadoEm], [ClienteCodigo]) values ('{InfoPlus_Descricao}', '{InfoPlus_Grupo}', '{InfoPlus_IdHeader}', '{InfoPlus_Obrigatorio}', '{InfoPlus_TipoInfoPlus}', '{InfoPlus_Valor}', '{datetime.now()}', '{Codigo_Cliente}');"

            exec_consulta_cliente_infoplus = cursor.execute(str_consulta_cliente_infoplus)
            try:
                # print(str_update_cliente_infoplus)
                key = cursor.fetchone()[0]
                exec_update = cursor.execute(str_update_cliente_infoplus)
                cursor.commit()
                print(f'{Codigo_Cliente} InfoPlus Atualizado')
            except TypeError:
                # print(str_insert_cliente_infoplus)
                exec_insert = cursor.execute(str_insert_cliente_infoplus)
                cursor.commit()
                print(f'{Codigo_Cliente} InfoPlus Adicionado')

            qtd_info_inseridos += 1
            if qtd_info_inseridos >= qtd_info_plus:
                break


        linhas_registros += 1
        #
        # i = linhas_registros
        # registros = i
        # if registros >= qtd_registro_webservice_cliente:
        #     print("\nFim da lista")
        #     break

def atualizadorCondPgto():
    # Get Condição de Pagamento
    link_post_condicao_pgto = link + 'Areas/Empresarial/Empresarial.svc/json/BuscarCondicoesPagamento'
    print(f'Buscar dados utilizando a URL: {link_post_condicao_pgto}')
    str_json_condicao_pgto = {
        "login": {
            "Base": base,
            "Usuario": user,
            "Senha": senha
        },
        "filtro": {
            "CondicaoCompra": False,
            "BuscarSomenteValidade": True
        }
    }

    # Estruturação
    dados_request_cond_pgto = requests.post(link_post_condicao_pgto, json = str_json_condicao_pgto)
    print(f'dados_request = {dados_request_cond_pgto}')  # Status da conexão, se 200 OK
    dados_parse_cond_pgto = xmltodict.parse(dados_request_cond_pgto.content)

    qtd_registro_webservice_cond_pgto = len(dados_parse_cond_pgto['LerCFRTsResponse']['LerCFRTsResult']['a:CFRT'])
    print(f'Qtd de campos de Filiais cadastrados na webservice: {qtd_registro_webservice_cond_pgto}')

    linhas_registros = 0
    while True:
        Codigo_Cond_Pgto = int(
            dados_parse_cond_pgto['LerCondicaoPagamentoResponse']['LerCondicaoPagamentoResult'][linhas_registros]['a:Codigo'])
        Nome_Cond_Pgto = str(
            dados_parse_cond_pgto['LerCondicaoPagamentoResponse']['LerCondicaoPagamentoResult'][linhas_registros]['a:Nome'])
        Descricao_Cond_Pgto = str(
            dados_parse_cond_pgto['LerCondicaoPagamentoResponse']['LerCondicaoPagamentoResult'][linhas_registros]['a:Descricao'])
        Nome_Vista = str(
            dados_parse_cond_pgto['LerCondicaoPagamentoResponse']['LerCondicaoPagamentoResult'][linhas_registros]['a:AVista'])

        """
        select * from [CondicaoPagamentos] where [Codigo] = '';
        update [CondicaoPagamentos] set [Nome] = '', [Descricao] = '', [Avista] = '', [AdicionaEm] = '' where [Codigo] = '';
        insert into [CondicaoPagamentos] ([Codigo], [Nome], [Descricao],  [Avista], [AdicionaEm]) values ('', '', '', '', '');
        """
        str_consulta_cliente = f"select * from [CondicaoPagamentos] where [Codigo] = '';"
        str_update_cliente = f"update [CondicaoPagamentos] set [Nome] = '', [Descricao] = '', [Avista] = '', [AdicionaEm] = '' where [Codigo] = '';"
        str_insert_cliente = f"insert into [CondicaoPagamentos] ([Codigo], [Nome], [Descricao],  [Avista], [AdicionaEm]) values ('', '', '', '', '');"



# Post tabela_preco
link_post_tabela_preco = link + 'Areas/Empresarial/Empresarial.svc/json/BuscarTabelasPreco'
print(f'Buscar dados utilizando a URL: {link_post_tabela_preco}')
str_json_tabela_preco = {
    "login": {
        "Base": base,
        "Usuario": user,
        "Senha": senha
    },
    "filtro": {
        "BuscarSomenteValidade": False,
        "Servico": True
    }
}

# Estruturação
dados_request_tabela_preco = requests.post(link_post_tabela_preco, json = str_json_tabela_preco)
print(f'dados_request = {dados_request_tabela_preco}')
dados_parse_tabela_preco = xmltodict.parse(dados_request_tabela_preco.content)

print(datetime.now())
print("Dados estruturados")

qtd_registro_webservice_tabela_preco = len(dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'])
print(f'Qtd de campos Tabelas de Preços cadastrados na webservice: {qtd_registro_webservice_tabela_preco}')

str_delete_tabela_preco = f"delete [TabelaPrecos];"
delete_tabela_preco = cursor.execute(str_delete_tabela_preco)
cursor.commit()
str_delete_item_tabela_preco = f"delete [ItemTabelaPrecos];"
delete_item_tabela_preco = cursor.execute(str_delete_item_tabela_preco)
cursor.commit()

linhas_registros = 57
while True:
    Codigo_tab_preco = dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:Codigo']
    Nome_tab_preco = dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:Nome']

    str_insert_tabela_preco = f"insert into [TabelaPrecos] ([Codigo], [Nome]) values ('{Codigo_tab_preco}', '{Nome_tab_preco}');"

    print(datetime.now())
    exec_insert = cursor.execute(str_insert_tabela_preco)
    cursor.commit()
    print(str_insert_tabela_preco)

    # FIXME: O Try está retirando o registro quando a quantidade é única, não salva o registro.
    try:
        len_item_tab_preco = len(dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:ItensTabelaPreco']['a:ItemTabelaPreco'])
        print(dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:ItensTabelaPreco']['a:ItemTabelaPreco'])
        print(f'Qtd de registro nesta tabela de preços: {len_item_tab_preco}')
        cont_item_tab_preco = 0
        for cont_item_tab_preco in range(0, len_item_tab_preco):
        # while True:
            try:
                print(f'[linhas_registros] :: {[linhas_registros]}. cont_item_tab_preco:: {cont_item_tab_preco}')
                CodigoItem_tab_preco = dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:ItensTabelaPreco']['a:ItemTabelaPreco'][cont_item_tab_preco]['a:CodigoItem']
                PrecoItem_tab_preco = dados_parse_tabela_preco['BuscarTabelasPrecoResponse']['BuscarTabelasPrecoResult']['a:TabelaPreco'][linhas_registros]['a:ItensTabelaPreco']['a:ItemTabelaPreco'][cont_item_tab_preco]['a:Preco']

                """
                select [CodigoItem], [CodigoTabelaPreco] from [ItemTabelaPrecos] where [CodigoItem] = '' and [CodigoTabelaPreco] = '';
                update [ItemTabelaPrecos] set [Preco] = '' where [CodigoItem] = '' and [CodigoTabelaPreco] = '';
                insert into [ItemTabelaPrecos] ([CodigoItem], [Preco], [CodigoTabelaPreco]) values ('', '', '');
                """

                # Definir as string de consulta, insert e update da Tabela de Preços
                str_insert_item_tabela_preco = f"insert into [ItemTabelaPrecos] ([Produto], [CodigoItem], [Preco], [CodigoTabelaPreco]) values ('0', '{CodigoItem_tab_preco}', '{PrecoItem_tab_preco}', '{Codigo_tab_preco}');"

                # Salvar dados dos Itens da Tabela de Preços no banco de dados
                print(datetime.now())
                exec_insert = cursor.execute(str_insert_item_tabela_preco)
                cursor.commit()
                print(str_insert_item_tabela_preco)

            # Except para erro ao tentar ler o item na tab de preço
            except KeyError:
                pass

            cont_item_tab_preco += 1
            # if cont_item_tab_preco >= len_item_tab_preco:
            #     break
    # Except para erro na leitura da quantidade de itens na tab de preços
    except TypeError:
        pass


    """[ItemTabelaPrecos]
      ,[CodigoItem]
      ,[Preco]
      ,[CodigoTabelaPreco]
    """

    linhas_registros += 1

    if linhas_registros >= qtd_registro_webservice_tabela_preco:
        print(datetime.now())
        print("Fim da lista")
        break

horario_final = datetime.now()
print(horario_final)
horario_duracao = horario_final - horario_inicio
print(f'\nDuração: {horario_duracao}')



# TODO:
# Incluir exception 'TimeoutError' da webservice
# Incluir exception 'ConnectTimeoutError' da webservice
# Incluir exception 'OperationalError' do banco de dados
# Incluir validação de login da webservice
# Incluir validação da base existente na webservice
# INcluir ultima data da atualização no filtro, para importar somente os cadastros de cliente que tiveram alteração
# Incluir DataUltimoReajuste na importação da tabela de preços para importar somente os que tiverem alteração
# Retirar a função de Try Except para identificar quando a consulta da tabela for vazia
