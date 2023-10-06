import requests
import credential
import time

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
        retorno = requests.post(URL_Validacao, json = Validar_Login)
        resposta_webservive = retorno.reason
        print(resposta_webservive)
        if resposta_webservive == "OK":
            break
        else:
            print(soneca)
            time.sleep(soneca)
            soneca += 30
    return resposta_webservive
            


