# DOCSTRING — Documentos das funções
# HELP — Função para mostrar os dados de ajuda da função

# help(len)


# O help ou docsctring das funções são inseridas entre pares aspas triplas.
def somar(*n):
    """
    Soma todos os valores contidos no parametro
    :param n: Inteiro ou Float a ser somado
    :return: O resultada da soma de 'n'
    """
    r = 0
    for x in n:
        r += x
    print(r)
    return r


somar(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
help(somar)


# Expressar um valor padrão ao parametro quando não for obrigatório
def escopoLocal(b, c):
    # Com 'global x' a variável x recebe o valor de fora da def e ignora o valor da def
    # global a
    # Quando usado global em uma def com parametro unico, o valor de return assume variavel global
    # O nome da var deve ser igual ao utilizado na def
    b = 2
    print(b, c)


a = 1
e = 5
escopoLocal(a, e)
print(a, e)


# Function 'retorn' gera um output no def, quando o print no console não é o objetivo.
def par(t):
    if t % 2 == 0:
        return True
    else:
        return False


print(par(6))


