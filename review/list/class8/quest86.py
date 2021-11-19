lista = list()
listb = list()

for i in range(0, 3):
    for j in range(0, 3):
        listb.append(int(input(f"Digite um valor para [{i}, {j}]: \n")))

    lista.append(listb[:])
    listb.clear()

for l in lista:
    print(l)
