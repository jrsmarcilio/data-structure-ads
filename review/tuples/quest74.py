from random import randint
tupla = []
counter = 0

while counter < 5:
    tupla.append(randint(0, 100))
    counter += 1

tupla = tupla(tupla)

print("Valores sorteados: ", end="")
for num in tupla:
    print(f"{num} ", end="")

smaller = tupla[0]
bigger = tupla[0]

for num in tupla:
    if num < smaller:
        smaller = num
    if num > bigger:
        bigger = num

print(f"\nMenor: {smaller}")
print(f"Maior: {bigger}")
