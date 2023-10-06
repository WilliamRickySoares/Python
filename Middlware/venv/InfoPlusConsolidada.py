import banco_middleware as bd
import WebserviceWK as wk
import credential
import time
import requests
import xmltodict
from loguru import logger
from datetime import datetime


horario_inicio = datetime.now()
# local_log = (f"c:/Des/log_infoplus/log_infoplus_{horario_inicio.year}{horario_inicio.month}{horario_inicio.day}_{horario_inicio.hour}{horario_inicio.minute}.txt")
local_log = ("c:/Des/log_infoplus/log_infoplus.txt")

logger.add = local_log
print(local_log)

# Documentação da API https://ajuda.wk.com.br/75/ws/index.htm#t=Apresentacao.htm

#Conctar banco middleware
banco = bd.conectar()

# Variaveis
teste = True  # Se True utiliza somente 1 registro da lista, Se False utiliza da fonte de dados
total = 1
interface_webservice = "http://totalmaxserv.ddns.net:9091/RadarWebWebServices/Areas/Empresarial/Empresarial.svc/json/"

while True:
    if wk.validar_login() == "OK":
        break

tipos_processos = [35, 48, 51] # Cadastro de serviços = 35; Cadastro de clientes = 48; Acomp. de serviços = 51

for t in tipos_processos:
    buscar_dados_info_plus = interface_webservice + 'BuscarDadosInfoPlus'
    logger.info(f"Tipo de Processo: {t}")
    tipoprocesso = {
        "login":
            {
                "Base": credential.base_webservice,
                "Usuario": credential.user_webservice,
                "Senha": credential.senha_webservice
            },
        "tipoProcesso": t
    }

    try:
        # print("request")
        dados_infoplus = requests.post(buscar_dados_info_plus, json = tipoprocesso)
    except requests.exceptions.ConnectTimeout:
        logger.error("Error ao solicitar na webservice (ConnectTimeout)")
        time.sleep(30)
        pass

    dados_infoplus_xml = dados_infoplus.content
    dado_infoplus = xmltodict.parse(dados_infoplus_xml)

    limite = len(dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'])
    logger.info(f'Qtd de campos de InfoPlus cadastrados do tipo de processo {t}: {limite}\n')

    lin = 0
    while True:
        InfoPlus_Descricao = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Descricao']
        InfoPlus_Grupo = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Grupo']
        InfoPlus_IdHeader = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:IdHeader']
        lin += 1

        InformacaoComplementarInfoPlus = interface_webservice + 'LerInformacaoComplementarInfoPlus'

        # Gera um novo número de código do InfoPlus, adicionando +1 ao último codigo
        i = 0
        while True:
            # Formata o terceiro termo
            i += 1
            if len(str(i)) < 3:
                termo = '0' * (3 - len(str(i)))
            else:
                termo = ''
            InfoPlus_Valor = f'{InfoPlus_Grupo}.{termo}{i}'
            json = {
                "login":
                    {
                        "Base": credential.base_webservice,
                        "Usuario": credential.user_webservice,
                        "Senha": credential.senha_webservice
                    },
                "Codigo": InfoPlus_Valor
            }
            try:
                retorno_complementar = requests.post(InformacaoComplementarInfoPlus, json = json)
            except requests.exceptions.ConnectTimeout:
                logger.error("Error ao solicitar na webservice")
                time.sleep(30)
                pass
            retorno_complementar_xml = retorno_complementar.content
            complementar_dict = xmltodict.parse(retorno_complementar_xml)
            codigo = complementar_dict['LerInformacaoComplementarInfoPlusResponse']['LerInformacaoComplementarInfoPlusResult']['a:Codigo']
            InfoPlus_Complementar = complementar_dict['LerInformacaoComplementarInfoPlusResponse']['LerInformacaoComplementarInfoPlusResult']['a:Descricao']

            # Interrupção do while de cada Complementar
            if not teste:
                if codigo is None:
                    break
            if teste:
                if codigo is None or i > 1:
                    break

            str_consulta_infoplus = f"select [Valor] from [InfoPlusConsolidadas] where Valor = '{InfoPlus_Valor}' and Grupo = '{InfoPlus_Grupo}' and [IdHeader] = '{InfoPlus_IdHeader}';"
            str_update_infoplus = f"update [InfoPlusConsolidadas] set [Complementar] = '{InfoPlus_Complementar}' where [Grupo] = '{InfoPlus_Grupo}' and [IdHeader] = '{InfoPlus_IdHeader}' and [Valor] = '{InfoPlus_Valor}';"
            str_insert_infoplus = f"insert into [InfoPlusConsolidadas] ([Descricao], [Grupo], [IdHeader], [Valor], [Complementar]) values('{InfoPlus_Descricao}', '{InfoPlus_Grupo}', '{InfoPlus_IdHeader}', '{InfoPlus_Valor}', '{InfoPlus_Complementar}');"
            exec_consulta_infoplus = banco.execute(str_consulta_infoplus)
            try:
                key = banco.fetchone()[0]
                exec_update = banco.execute(str_update_infoplus)
                banco.commit()
                # print(str_update_infoplus)
                logger.info(f'InfoPlus | {InfoPlus_Descricao} | {InfoPlus_Valor} | {InfoPlus_Complementar} || Atualizado')
            except TypeError:
                exec_insert = banco.execute(str_insert_infoplus)
                banco.commit()
                # print(str_insert_infoplus)
                logger.info(f'InfoPlus | {InfoPlus_Descricao} | {InfoPlus_Valor} | {InfoPlus_Complementar} || Adicionado')

        # Interrupção do while do tipo de processo
        b = i - 1
        logger.info(f"Qtd de de InfoPlusComplementares do grupo {InfoPlus_Descricao}: {b}\n")

        total += b
        if lin >= limite:
            break

horario_fim = datetime.now()
logger.info(f"Total de InfoPlus Importadas: {total} | {horario_fim}")
logger.info(f"Fim da geração! {horario_fim - horario_inicio}")
