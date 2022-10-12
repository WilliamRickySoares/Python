"""Desafio 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato.
"""

jogadores = dict()
gol_partidas = list()

jogadores['nome_jogador'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
jogadores['qtd_partidas'] = int(input(f"Quantas partidas {jogadores['nome_jogador']} participou: "))

print("-=" * 30)
for i in range(0, jogadores['qtd_partidas']):
    gol_partidas.append(int(input(f"Gols do {jogadores['nome_jogador']} na {i + 1}º partida: ")))
jogadores['gols_campeonato'] = gol_partidas[:]

jogadores['total_gols'] = 0
for g in jogadores['gols_campeonato']:
    jogadores['total_gols'] += g

print(f"\nO jogador {jogadores['nome_jogador']} participou de {jogadores['qtd_partidas']} partidas e"
      f" realizou {jogadores['total_gols']} gols no campeonato.")

print(f"\nO jogador {jogadores['nome_jogador']} fez:")
for i, j in enumerate(jogadores['gols_campeonato']):
    print(f"Na {i + 1}º partida {j} gol(s).")

print("-=" * 30)
print(jogadores)
