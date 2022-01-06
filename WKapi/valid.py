import zeep

wsdl = 'http://webservices.wk.com.br/Areas/Empresarial/Empresarial.svc?singleWsdl'
client = zeep.Client(wsdl=wsdl)
print(client.service.Method1('Zeep', 'is cool'))
print(wsdl)
