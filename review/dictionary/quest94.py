person_dict = dict()
general_info, names, names_quantity, ages, women, above_mean = list(
), list(), list(), list(), list(), list()

while True:
    person_dict['name'] = input("Nome: \n")

    sex = input("Sexo [M/F]: \n")
    sex = sex[0].upper()
    person_dict['sex'] = sex

    person_dict['age'] = float(input("Idade: \n"))

    general_info.append(person_dict.copy())

    leave = input("Continuar? [S/N] \n")
    leave = leave.upper()
    if leave[0] == "N":
        break

for dictionary in general_info:
    names_quantity.append(dictionary.get("name"))

    ages.append(dictionary.get("age"))
    age_mean = sum(ages)/len(ages)

    for key, value in dictionary.items():
        if value == "F":
            women.append(dictionary.get("name"))

    if dictionary.get("age") > (age_mean):
        above_mean.append(dictionary.get("name"))

print(f"Pessoas cadastradas: {len(names_quantity)}")
print(f"Idade média do grupo: {age_mean:.1f} anos.")
print(f"Mulheres do grupo: {women}")
print(f"Pessoas com idade acima da média: {above_mean}")
