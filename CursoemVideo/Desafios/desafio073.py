print("""Desafio 073 (M3A16)
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem da colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Uma lista com os times em ordem alfabetica;
d) Em que posição na tabela está o time da 'Chapecoense';""")

times = ('Flamengo', 'Atletico-MG', 'Palmeiras', 'Santos', 'Gremio', 'Sao Paulo',
         'Corinthians', 'Fluminense', 'Athletico-PR', 'Internacional',
         'Sport', 'Cruzeiro', 'Chapecoense', 'Bahia', 'Botafogo-RJ', 'Coritiba',
         'Vasco', 'Vitoria', 'Goias', 'Ceara', 'Fortaleza', 'Ponte Preta',
         'Atletico-GO', 'Bragantino', 'Figueirense', 'America-MG', 'Avai',
         'Santa Cruz', 'Juventude', 'Cuiaba', 'Criciuma', 'Joinville', 'CSA', 'Parana')

print(f'\na) Os 5 primeiros colocados são', end=' ')
cont = 0
for pri in times[:5]:
    cont += 1
    if cont == 5:
        print(str(pri), end='.')
    elif cont == 4:
        print(str(pri), end=' e ')
    else:
        print(str(pri), end=', ')

print(f'\nb) Os 4 lanterninhas são ', end='')
cont = 0
for ult in times[-4:]:
    cont += 1
    if cont == 4:
        print(str(ult), end='.')
    elif cont == 3:
        print(str(ult), end=' e ')
    else:
        print(str(ult), end=', ')

print('\nc) De forma ordenada os times são ', end='')
cont = 0
for sort in sorted(times):
    cont += 1
    if cont == len(times):
        print(str(sort), end='.')
    elif cont == len(times) - 1:
        print(str(sort), end=' e ')
    else:
        print(str(sort), end=', ')

print(f'\nd) O Chapecoense está na {times.index("Chapecoense") + 1}º posição.')
