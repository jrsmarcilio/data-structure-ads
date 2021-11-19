tupla = (
    "Galadriel", "Luthien Tinuviel", "Erik Killmonger",
    "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda"
)
vowels = ["a", "e", "i", "o", "u"]

for name in tupla:
    name = str(name).lower()
    lista = []

    for letter in name:
        for i in vowels:
            if letter == i:
                lista.append(letter)

    print(f"{name.capitalize()}: {lista} - {len(lista)} vogais")
    del(lista)
