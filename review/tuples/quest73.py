teams = (
    "Atlético", "Flamengo", "Corinthians", "Palmeiras", "Fluminense",
    "América-MG", "São Paulo", "Grêmio", "Vasco da Gama", "Botafogo",
    "Sport Recife", "Cruzeiro", "EC Vitória", "Santos", "Chapecoense",
    "Atlético-PR", "Internacional", "Bahia", "Ceará SC", "Paraná"
)
print(f"Primeiros 5 colocados do Brasileirão: \n{teams[0:6]}")
print(f"Últimos 4 colocados: \n{teams[-4:]}")
print(f"\Times em ordem alfabética: \n")
for time in sorted(teams):
    print(time)
chapecoensePosition = teams.index("Chapecoense") + 1
print(f"A Chapecoense está na {chapecoensePosition}ª posição.")
