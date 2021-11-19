worker_infos = dict()

name = input("Digite um nome: \n")
birthday = input("Data de nascimento: \n")
ctps = int(input("Número da carteira de trabalho (CTPS): \n"))

retirement_age = int()
age = int()


worker_infos["name"] = name
worker_infos["birthday"] = birthday
worker_infos["ctps"] = ctps

if ctps != 0:
    hiring_date = input("Data de contratação: \n")
    salary = int(input("Salário: \nR$ "))
    
    worker_infos["hiring date"] = hiring_date
    worker_infos["salary"] = salary

print(worker_infos)
