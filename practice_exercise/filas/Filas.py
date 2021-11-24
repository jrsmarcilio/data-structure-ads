# Programa 6.7 - Simulação de uma fila de banco
class Filas:
    def __init__(self):
        self.items = [ "Miguel", "Nicole", "Heitor", "Helena", "Alice" ]

    def isEmpty(self):
        return self.items == [] 

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

fila = Filas()

while True:
    print(f"\nExistem {fila.size()} clientes na fila")
    print(f"\nFila atual: {fila.items}")
    print(f"\nDigite:\nF para adicionar um cliente ao fim da fila,")
    print("A para realizar o atendimento.\nS para sair.")
    op = input("Operação (F, A ou S):").upper()
    if op == "A":
        if fila.size() > 0:
            atendido = fila.dequeue()
            print(f"Cliente {atendido} atendido")
        else:
            print("Fila vazia! Ninguém para atender.")
    elif op == "F":
        paciente = input("Digite o nome paciente >>> ")
        fila.enqueue(paciente)
    elif op == "S":
        break
    else:
        print("Operação inválida! Digite apenas F, A ou S!")