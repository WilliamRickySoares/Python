import requests
import csv
import xmltodict

# Variaveis
base = "WSTotal"
user = "WebService"
senha = "Fusion_100%$"

link_post = "https://webservices.wk.com.br/Areas/Empresarial/Empresarial.svc/json/ValidarLogin"
login = {
    "login":
        {
            "Base": base,
            "Usuario": user,
            "Senha": senha
        }
}
dados_infoplus = requests.post(link_post, json = login)
dados_infoplus_xml = dados_infoplus.content
dado_infoplus = xmltodict.parse(dados_infoplus_xml)
print(dados_infoplus)
