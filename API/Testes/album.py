from zeep import Client
import operator

wsdl = 'http://webservices.Amazon.com/AWSECommerceService/AWSECommerceService.wsdl'
client = Client(wsdl)

# get each operation signature
for service in client.wsdl.services.values():
    print("service:", service.name)
    for port in service.ports.values():
        operations = sorted(
            port.binding._operations.values(),
            key=operator.attrgetter('name'))

        for operation in operations:
            print("method :", operation.name)
            print("  input :", operation.input.signature())
            print()
    print()

# get a specific type signature by name
complextype = client.get_type('ns0:CartGetRequest')
print(complextype.name)
print(complextype.signature())
