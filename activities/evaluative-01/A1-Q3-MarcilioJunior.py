# Crie um programa que armazene em uma tupla os meses do ano e informe o mês por
# extenso. Por exemplo, se o usuário digitar 6 o programa deve exibir junho. Se ele digitar um valor menor que 1 e maior que 13, o programa deve exibir uma mensagem de erro.

month = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

while True:
    n = int(input("Digite o número do mês: >>> "))
    if n >= 1 and n <= 12:
        print(f"Você digitou: {month[n-1]}.")
        break
    else:
        print("Valor incorreto, tente novamente.", end=" ")
