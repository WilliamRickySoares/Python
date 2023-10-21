print("Atualizador iniciado")

import requests
from datetime import datetime
import warnings
warnings.filterwarnings("ignore", category = DeprecationWarning)

# Variaveis
print(datetime.now())
print("Variáveis definidas")

# Filial
link_post = "http://maxservrr.ddns.net:8181/RadarWebService/Areas/Empresarial/Empresarial.svc/json/BuscarFiliais"
print(f'Buscar dados utilizando a URL: {link_post}')
str_json = {
    "login": {
        "Base": 'Total',
        "Usuario": 'WebService',
        "Senha": 'Fusion_100%$'
    },
    "filtro": {
        "IncluirFiliaisInativas": True
    }
}

# Estruturação
dados_request = requests.get(link_post, json = str_json)
print(f'dados_request = {dados_request}')
# dados_parse = xmltodict.parse(dados_request.content)
# print(dados_parse)
# print(datetime.now())
# print("Dados estruturados")

