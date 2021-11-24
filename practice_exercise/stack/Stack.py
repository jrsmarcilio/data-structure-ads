class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def menu(self):
        while True:
            print("\nPilha atual: ", self.items)
            print("\nE - Empilhar elemento")
            print("D - Desempilhar elemento")
            print("S - Sair")
            op = input("\nDigite uma opção: ").upper()
            if op == "E":
                item = input("Digite o item: ")
                self.push(item)
            elif op == "D":
                self.pop()
            elif op == "S":
                break


stack = Stack()
stack.menu()


def parentheseChecker(parentheses):
    stack = Stack()
    for par in parentheses:
        if par == "(":
            stack.push(par)
        else:
            if stack.isEmpty():
                return False
            else:
                stack.pop()

    if (stack.isEmpty()):
        return True
    else:
        return False


print('\nQuest 03 - Verificador de Emparelhamento de Parênteses')
print("()() - ", parentheseChecker("()()"))
print("(() - ", parentheseChecker("(()"))
print(")( - ", parentheseChecker(")("))
print("() - ", parentheseChecker("()"))
