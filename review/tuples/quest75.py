counter = 1
tupla = []

while counter < 5:
    n = int(input(f"Digite um número ({counter}/4): \n"))
    tupla.append(n)
    counter += 1

tupla = tuple(tupla)
print(f"Tupla: {tupla}")

nine = tupla.count(9)
print(f"O valor 9 aparece {nine} vezes.")

if 3 in tupla:
    print(f"O primeiro 3 está na posição: {tupla.index(3)+ 1}.")
else:
    print("O número 3 não está presente.")

pairs = []
for num in tupla:
    if num % 2 == 0:
        pairs.append(num)
print(f"Números pares: {pairs}")

