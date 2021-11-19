listing = (
    "pão", 1,
    "leite", 3.50,
    "frango", 10.90
)

print("=" * 35)
print("Tela preta, letra verde.")
print("=" * 35)

product = 0
price = 1

for item in range(0, len(listing) // 2):
    print(f"{listing[product]:.<30} R${listing[price]:>7.2f}")
    price += 2
    product += 2
