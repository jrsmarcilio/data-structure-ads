lista = list()
listb = list()
counter = 0

while True:
    lista.append(str(input("Nome: \n")))
    lista.append(float(input("Peso (em kg): \n")))

    listb.append(lista[:])
    lista.clear()
    counter += 1

    pergunta = str(input("Continuar? [Sim/Não] \n")).upper()
    if pergunta[0] == "N":
        break

print(f"a) pessoas cadastradas: {counter}.")

pesos = list()

for i in listb:
    pesos.append(i[1])

pesos = sorted(pesos)

menor = pesos[0]
maior = pesos[-1]

mais_pesados = list()
menos_pesados = list()

for k in listb:
    if k[1] == maior:
        mais_pesados.append(k[0])
    if k[1] == menor:
        menos_pesados.append(k[0])

print(f" b) O maior peso foi de {maior}kg. Peso de {mais_pesados}")
print(f" c) O menor peso foi de {menor}kg. Peso de {menos_pesados}.")
