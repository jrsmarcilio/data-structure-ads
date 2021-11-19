# Crie uma tupla com os 15 primeiros países com mais medalhas no ranking das olimpíadas do Japão (2021). Informe nesta lista:
# i. os 3 primeiros colocados;
# ii. os 2 últimos colocados;
# iii. e se o Brasil ficou entre esses 15 primeiros países, se sim em que posição ficou.

rank_olympiad = (
    "United States of America",
    "People's Republic of China",
    "Japan",
    "Great Britain",
    "ROC",
    "Australia",
    "Netherlands",
    "France",
    "Germany",
    "Italy",
    "Canada",
    "Brazil",
    "New Zealand",
    "Cuba",
    "Hungary",
)

print('Os 3 primeiros colocados foram: \n', rank_olympiad[0 : 3])
print('-' * 20)
print('Os 2 últimos colocados foram: \n', rank_olympiad[13 : 15])
print('-' * 20)

while True:
  str_team = 'Brazil'
  try:
    if (rank_olympiad.index(str_team)):
      print(f'O país {str_team} está na posição:', rank_olympiad.index(str_team))
      break
  except ValueError:
    print(f'O país {str_team} não está na lista')
    break
