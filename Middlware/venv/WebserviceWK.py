import requests
import credential
import time
from loguru import logger

def validar_login():
    servidor_webservice = "http://totalmaxserv.ddns.net:9091"
    interface_webservice = "/RadarWebWebServices/Areas/Empresarial/Empresarial.svc/json"
    classes_validacao = "/ValidarLogin"
    soneca = 30
    URL_Validacao = servidor_webservice + interface_webservice + classes_validacao
    Validar_Login = {
        "login":
            {
                "Base": credential.base_webservice,
                "Usuario": credential.user_webservice,
                "Senha": credential.senha_webservice
            }
    }

    while True:
        try:
            logger.info("Testando a conexão à webservice")
            retorno = requests.post(URL_Validacao, json = Validar_Login)
            resposta_webservive = retorno.reason
            if resposta_webservive == "OK":
                logger.info(f"Conexão ao webservice {resposta_webservive}")
            return resposta_webservive
            break
        except:
            logger.warning("Falha ao testar a conexão à webservice")
            logger.info(f"Esperar por {soneca}")
            time.sleep(soneca)
            soneca += 30
