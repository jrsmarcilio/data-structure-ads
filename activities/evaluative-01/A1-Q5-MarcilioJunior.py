# Faça um programa que preencha uma lista contendo um número indefinido de nome de carros e seus consumos (quantos km cada carro faz com 1 litro de combustível)Calcule e mostre:
# a. O modelo de carro mais econômico
# b. O modelo de carro menos econômico
# c. Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma distância de 1000 km

cars = list()
info_car = {'model': '', 'consumption': 0}

while True:
    info_car['model'] = input('Modelo: >>> ')
    info_car['consumption'] = float(
        input('Qnt km por 1l de combustível? >>> '))
    cars.append(info_car.copy())
    info_car['model'] = ''
    info_car['consumption'] = 0
    option = input('Você quer continuar? [Y/N] ')
    if option in 'Nn':
        break

# info_car['model'] = 'Fusca'
# info_car['consumption'] = 8
# cars.append(info_car.copy())
# info_car['model'] = 'Gol'
# info_car['consumption'] = 10
# cars.append(info_car.copy())
# info_car['model'] = 'Palio'
# info_car['consumption'] = 7
# cars.append(info_car.copy())

for car in cars:
    for k, v in car.items():
        print(f"{k}: {v}")
    print(
        f"O {car['model']} para percorrer 1000 km consome {1000 / car['consumption']} litros de combustível")
    print("-" * 20)

moreEconomical = max(cars, key=lambda x: x['consumption'])
lessEconomical = min(cars, key=lambda x: x['consumption'])

print(
    f"O carro mais econômico é o {moreEconomical['model']} que faz {moreEconomical['consumption']} km por litro de combustível")

print(
    f"O carro menos econômico é o {lessEconomical['model']} que faz {lessEconomical['consumption']} km por litro de combustível")

# reference >>> https://www.hashtagtreinamentos.com/funcoes-lambda-python?gclid=CjwKCAjwk6-LBhBZEiwAOUUDp7nI99Y2LYCg8lgpfzaYf3VvQtR9LQSIG7yhO5Tnsp3oPpuC3vr44xoCykwQAvD_BwE
