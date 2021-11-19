aproveitamento = dict()
gols_total = 0

aproveitamento['nome'] = input("Qual o nome do(a) jogador(a)? \n" )

aproveitamento['partidas'] = int(input("Partidas jogadas: \n"))

for partida in range(aproveitamento['partidas']):
    gols_partida = int(input(f"Quantos gols o jogador {aproveitamento['nome']} fez na partida {partida +1}? \n"))
    gols_total += gols_partida
aproveitamento['gols_total'] = gols_total

print(
    f"O jogador {aproveitamento['nome']} jogou {aproveitamento['partidas']} partidas e fez um total de {aproveitamento['gols_total']} gols."
)