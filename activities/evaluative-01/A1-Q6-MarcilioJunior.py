# 6. Duas pessoas estão se conhecendo e responderam a seguinte pergunta: “o que você gosta de fazer no seu tempo livre?” A resposta de cada uma das pessoas foi armazenada em uma lista de lazer. Responda o que se pede:

leisure_list = list()
people = {'name': '', 'response': ''}

people['name'] = "Google Assistente"
# "Eu gosto de passar o tempo lendo poesia."
people['response'] = "LER"
leisure_list.append(people.copy())

people['name'] = "Alexa"
# "Eu gosto de cantar e de aprender coisas novas."
people['response'] = "CANTAR"
leisure_list.append(people.copy())

# a. Quais os lazeres que as pessoas possuem em comum?
exists_in_common = leisure_list[0]['response'] in leisure_list[1]['response']

if exists_in_common:
    print("As pessoas possuem em comum, o gosto por " +
          leisure_list[0]['response'])

if not exists_in_common:
    print("Não existem lazeres em comum.")

# b. O que somente a primeira pessoa gosta de fazer no seu tempo livre?
# c. O que somente a segunda pessoa gosta de fazer no seu tempo livre?

for i in range(len(leisure_list)):
    print(
        f"\n{leisure_list[i]['name']} gosta de {leisure_list[i]['response']} no seu tempo livre.")

# d. O que as duas pessoas gostam de fazer no seu tempo livre?

print(
    f"\n{leisure_list[i]['name']} gosta de {leisure_list[i]['response']} no seu tempo livre. Enquanto {leisure_list[i]['name']} gosta de {leisure_list[i]['response']}."
)
