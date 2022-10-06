"""Desafio 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluíndo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

jogadores = dict()
gol_partidas = list()
time = list()

while True:
    jogadores['nome_jogador'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
    jogadores['qtd_partidas'] = int(input(f"Quantas partidas {jogadores['nome_jogador']} participou: "))

    print("")
    for i in range(0, jogadores['qtd_partidas']):
        gol_partidas.append(int(input(f"Gols do {jogadores['nome_jogador']} na {i + 1}º partida: ")))
        # print(gol_partidas)
    jogadores['gols_campeonato'] = gol_partidas[:]
    gol_partidas.clear()

    jogadores['total_gols'] = 0
    for g in jogadores['gols_campeonato']:
        jogadores['total_gols'] += g

    time.append(jogadores.copy())
    # print(gol_partidas)

    while True:
        q = str(input("Adicionar outro jogador? [S/N] ")).strip().lower()[0]
        if q in "SsNn":
            break
    if q in "Nn":
        break
    print("")

num = 1
for j in time:
    print(f"{num:^4}--- {j['nome_jogador']:-<20}-- {j['total_gols']:>4}")
    num += 1
