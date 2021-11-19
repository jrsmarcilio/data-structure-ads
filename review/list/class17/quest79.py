lista = []
while True:
    num = int(input("Digite um número: \n"))
    if num in lista:
        print("O número já está na lista.")
    else:
        lista.append(num)
        print("Adicionado com sucesso...")

    keep = str(input("Quer continuar [SIM / NÃO]? \n")).strip().upper()
    if keep[0] == "N":
        break
    elif keep[0] == "S":
        print("Continuando.")
    else:
        print("Digite apenas 'sim' ou 'não'!")

lista.sort()
print(f"Você digitou os valores {lista}!")
