from parsel import Selector
from httpx import get

saltar_linha = ['</li>', '   ', '</pre>', '</p>']

especiais = [('<strong>', 'negrito'),
             ('<em>', 'italico'),
             ('"u">', 'italico')]


def Substituir(texto_original):
    remover = ["class=", '"gap">', 'gab', "<li ", "<li>","</li>", "<ul>", "</ul>", '<p ', '</p>', "<span ", "</span>",
               '"anchor"', 'style="list-style-type:none">', '<ol', '</ol>', 'type="a">', 'type="i">', '"line862">', '"line891">', '<strong>',
               '</strong>', '<em>', '</em>', '<pre>', '</pre>', '"u">']
    for termo in remover:
        if termo in texto_original:
            texto_ajustado = texto_original.replace(termo, "")
            texto_original = texto_ajustado

    while "id=" in texto_original:
        ini = texto_original.index("id=")
        parte_inicial = texto_original[ini:]
        fin = parte_inicial.index('">')
        parte_dinamica = (f'{texto_original[ini:fin + ini]}">')
        texto_ajustado = texto_original.replace(parte_dinamica, "")
        texto_original = texto_ajustado.lstrip().rstrip()
    return texto_original


link_base = 'https://wiki.python.org.br'
link_lista_exercicios = '/ListaDeExercicios'
conteudo = get(link_base + link_lista_exercicios).content
sel = Selector(text = conteudo.decode())

titulo_pagina = sel.css('title::text').get() # Titulo
print(titulo_pagina)

nome_exercicios = sel.css('ol').css('a::text').getall()
print(nome_exercicios)

for link_pagina in nome_exercicios:
    numero_arquivo = 0
    print(link_base + '/' + link_pagina)
    pagina_questionario = conteudo = get(link_base + '/' + link_pagina).content
    sel_sub = Selector(text = conteudo.decode())
    lista_questao = sel_sub.xpath('//li[(@class="gap")]').getall()
    for questao in lista_questao:

        numero_arquivo += 1
        nome_arquivo = f'{link_pagina}{numero_arquivo:02}.py'
        titulo = (f'# {numero_arquivo} ')
        arquivo = open(nome_arquivo, 'x')
        arquivo.writelines(f'## {titulo_pagina} ##')
        arquivo.writelines(f'\n# {link_pagina} - {titulo}')

        questao_ajustada = Substituir(questao)
        linha_quebrada = questao_ajustada.split('  ')
        for frase in linha_quebrada:
            if len(frase) != 0:
                print('# ', end = '')
                resultado = frase.strip()
                print(resultado)
                arquivo.writelines(f"\n# {resultado}")
        arquivo.close()



## TODO: Validar se o site está respondendo antes de iniciar a leitura e preenchimento




