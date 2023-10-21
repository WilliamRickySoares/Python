import requests
import html


r = requests.get(
    'https://webservices.wk.com.br/Areas/Empresarial/Empresarial.svc/json/ValidarLogin')
print(r)
print(r.json())
