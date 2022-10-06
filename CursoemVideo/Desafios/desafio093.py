"""Desafio 093
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e
quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
guardado em um dicionário, incluíndo o total de gols feitos durante o campeonato.
"""

campeonato = dict()
gol_partidas = list()

campeonato['nome_jogador'] = str(input("Digite o nome do jogador: ")).strip().capitalize()
campeonato['qtd_partidas'] = int(input(f"Quantas partidas {campeonato['nome_jogador']} participou: "))

print("")
for i in range(0, campeonato['qtd_partidas']):
    gol_partidas.append(int(input(f"Gols do {campeonato['nome_jogador']} na {i + 1}º partida: ")))
campeonato['gols_campeonato'] = gol_partidas

campeonato['total_gols'] = 0
for g in campeonato['gols_campeonato']:
    campeonato['total_gols'] += g


print(f"\nO jogador {campeonato['nome_jogador']} participou de {campeonato['qtd_partidas']} partidas e"
      f" realizou {campeonato['total_gols']} gols no campeonato.")

print(campeonato)
