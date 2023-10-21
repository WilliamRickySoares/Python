import requests
import csv
import xmltodict

# Variaveis
teste = False
total = 1
nome_arquivo = 'InfoPlusConsolidada.csv'
cabecalho = "[Descricao], [Grupo], [idHeader], [Valor], [Complementar]"
base = "TOTAL"
user = "FUSION"
senha = "GsiTNjR*@LuoL3"
link = "http://totalmaxserv.ddns.net:9091/RadarWebWebServices/"

# Cadastro de serviços = 35;
# Cadastro de clientes = 48;
# Acomp. de serviços = 51
tipos_processos = [35, 48, 51]

for t in tipos_processos:
    buscar_dados_info_plus = link + 'Areas/Empresarial/Empresarial.svc/json/BuscarDadosInfoPlus'
    print(f"Tipo de Processo: {t}")
    tipoprocesso = {
        "login":
            {
                "Base": base,
                "Usuario": user,
                "Senha": senha
            },
        "tipoProcesso": t
    }
    dados_infoplus = requests.post(buscar_dados_info_plus, json = tipoprocesso)
    dados_infoplus_xml = dados_infoplus.content
    dado_infoplus = xmltodict.parse(dados_infoplus_xml)

    limite = len(dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'])
    print(f'Qtd de campos de InfoPlus cadastrados: {limite}')

    lin = 0
    while True:
        descricao = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Descricao']
        grupo = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Grupo']
        id_header = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:IdHeader']
        obrigatorio = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Obrigatorio']
        valor = dado_infoplus['BuscarDadosInfoPlusResponse']['BuscarDadosInfoPlusResult']['a:InfoPlus'][lin]['a:Valor']
        lin += 1

        InformacaoComplementarInfoPlus = link + 'Areas/Empresarial/Empresarial.svc/json/LerInformacaoComplementarInfoPlus'

        i = 0
        while True:
            # Formata o terceiro termo
            i += 1
            if len(str(i)) < 3:
                termo = '0' * (3 - len(str(i)))
            else:
                termo = ''
            codigo_complementar = f'{grupo}.{termo}{i}'
            json = {
                "login":
                    {
                        "Base": base,
                        "Usuario": user,
                        "Senha": senha
                    },
                "Codigo": codigo_complementar
            }
            retorno_complementar = requests.post(InformacaoComplementarInfoPlus, json = json)
            retorno_complementar_xml = retorno_complementar.content

            complementar_dict = xmltodict.parse(retorno_complementar_xml)
            codigo = complementar_dict['LerInformacaoComplementarInfoPlusResponse']['LerInformacaoComplementarInfoPlusResult']['a:Codigo']
            complementar = complementar_dict['LerInformacaoComplementarInfoPlusResponse']['LerInformacaoComplementarInfoPlusResult']['a:Descricao']

            if not teste:
                if codigo is None:
                    break

            if teste:
                if codigo is None or i > 1:
                    break

            rows = (descricao, grupo, id_header, codigo, complementar)
            insert = [f'insert into [InfoPlusConsolidadas] ({cabecalho}) values {rows};']
            print(insert)

            with open(nome_arquivo, 'a', newline = '') as file:
                writer_file = csv.writer(file)
                writer_file.writerow(insert)
                file.close()
        b = i - 1
        print(f"Qtd de de InfoPlusComplementares do grupo {descricao}: {b}\n")

        total += b
        if lin >= limite:
            break

# A Cortesia do Cliente fica fora do padrão dos demais InfoPlus, inserir de forma manual
with open(nome_arquivo, 'a', newline = '') as file:
    rows_cortesia = ('Cortesia', '2.08', '357', '2.08', 'SIM')
    insert_cortesia = [f'insert into [InfoPlusConsolidadas] ({cabecalho}) values {rows_cortesia};']
    writer_file = csv.writer(file)
    writer_file.writerow(insert_cortesia)
    file.close()

with open(nome_arquivo) as f:
    newText = f.read().replace('"', '')
with open(nome_arquivo, "w") as f:
    f.write(newText)

print(f"Total de InfoPlus Importadas {total}"
      f"\nFim da geração!")
