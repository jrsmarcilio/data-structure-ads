# Crie um dicionário que armazene o nome de um álbum, o artista e o seu ano de lançamento. Imprima as informações armazenadas no dicionário.

band = {"artist": "", "album": "", "": 0}

band["artist"] = "Red Hot Chili Peppers"
band["album"] = "CALIFORNICATION"
band["year"] = 1999

for k, v in band.items():
    print(f"{k}: {v}")
