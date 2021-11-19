aproveitamento = dict()
gols, soma_gols, cod = 0, 0, 0
lista_gols, infos_jogadores = list(), list()

while True:
    aproveitamento['nome'] = input("Qual o nome do(a) jogador(a)? \n")
    nome_jogador = aproveitamento['nome']

    cod += 1
    aproveitamento['cod'] = cod

    aproveitamento['partidas'] = int(input("Partidas jogadas: \n"))
    partidas_jogadas = aproveitamento['partidas']

    for partida in range(partidas_jogadas):
        gols_partida = int(
            input(f"Quantos gols {nome_jogador} fez na partida {partida+1}? \n"))
        lista_gols.append(gols_partida)
        aproveitamento['lista_gols'] = lista_gols.copy()

    aproveitamento['soma_gols'] = sum(lista_gols)

    infos_jogadores.append(aproveitamento.copy())
    lista_gols.clear()

    continuar = input("Quer continuar? [S/N] \n")
    continuar = continuar.upper()
    if continuar[0] == "N":
        break

print(f"{'cod':^5} {'nome':^10} {'gols':<25} {'total':<25}")
for jogador in infos_jogadores:
    print(f"{jogador['cod']!s:^5s} {jogador['nome']!s:^10s} {jogador['lista_gols']!s:<25s} {jogador['soma_gols']!s:<25s}")

while True:
    cod_usuario = int(
        input("Mostrar dados de qual jogador? (999 para parar) \n"))

    if cod_usuario == 999:
        break
    if cod_usuario > len(infos_jogadores):
        print("Erro! Não existe jogador com esse código. Tente novamente!")
    for dictionary in infos_jogadores:
        if dictionary['cod'] == cod_usuario:
            print(f"Levantamento do jogador {dictionary['nome'].upper()}:")
            for n, gol in enumerate(dictionary['lista_gols']):
                print(f"No jogo {n+1}, fez {gol} gols.")
