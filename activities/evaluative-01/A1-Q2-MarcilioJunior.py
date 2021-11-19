# Utilizando o dicionário da questão 1, crie uma lista de álbuns disponíveis em um aplicativo de streaming de músicas. Imprima todas os álbuns que foram armazenados.

musicAmazon = list()
band = {"artist": "", "album": "", "year": 0}

band["artist"] = "Red Hot Chili Peppers"
band["album"] = "CALIFORNICATION"
band["year"] = 1999
musicAmazon.append(band.copy())

band["artist"] = "Guns N' Roses"
band["album"] = "APPETITE FOR DESTRUCTION"
band["year"] = 1964
musicAmazon.append(band.copy())

band["artist"] = "Nirvana"
band["album"] = "NEVERMIND (REMASTERED)"
band["year"] = 1991
musicAmazon.append(band)

for band in musicAmazon:
    for k, v in band.items():
        print(f"{k}: {v}")
    print("-" * 20)
