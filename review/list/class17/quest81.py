lista = []

while True:
    lista.append(int(input("Digite um número: \n")))
    cont = str(input("Quer continuar? \n")).strip().upper()
    if cont[0] == "S":
        print("Continuando.")
    elif cont[0] == "N":
        print("Programa finalizado.")
        break
    else:
        print("Digite uma resposta válida.")

print(f"{len(lista)} números foram digitados.")

lista.sort(reverse=True)
print(f"Esta é a lista ordenada decrescentemente {lista}")

if 5 in lista:
    print(f"O valor 5 foi digitado.")
else:
    print("O valor 5 não foi digitado.")
