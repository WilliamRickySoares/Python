"""Desafio 095
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluíndo um sistema de visualização de detalhes
do aproveitamento de cada jogador.
"""

jogadores = {'num': 0}
gol_partidas = list()
time = list()

while True:
    jogadores['nome_jogador'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
    jogadores['qtd_partidas'] = int(input(f"Quantas partidas {jogadores['nome_jogador']} participou: "))
    jogadores['num'] += 1
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

    print("")
    while True:
        q = str(input("Adicionar outro jogador? [S/N] ")).strip().lower()[0]
        if q in "SsNn":
            break
        print("Favor escolher entre 'Sim' ou 'Não'!")
    if q in "Nn":
        break
    print()


print("========= TABELA DOS JOGADORES =========")
for j in time:
    print(f"{j['num']:>3} - {j['nome_jogador']:<15} {j['gols_campeonato']} {'':>5}{j['total_gols']:>3}")
print("=" * 40)
print()

print("=" * 40)
while True:
    q = int(input("Qual jogador deseja ver os detalhes? (Digite 999 para sair) "))
    if q >= len(time):
        print(f"Código de Jogador não encontrado, favor escolher até o número {len(time)}.")
    if q == 999:
        break
    print()
    print(f"=========== TABELA JOGADOR {q} ===========")
    print(f"O jogador {q} - {time[q - 1]['nome_jogador']} partipou de {time[q - 1]['qtd_partidas']} "
          f"partidas e totalizou {time[q - 1]['total_gols']} gols no campeonato.")
    print("=" * 40)
    print()
print()
