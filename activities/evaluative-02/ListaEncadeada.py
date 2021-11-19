class NodoLista:
    def __init__(self, dado=0, proximo_nodo=None):
        self.dado = dado
        self.proximo = proximo_nodo

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def __repr__(self):
        return "[" + str(self.cabeca) + "]"

    def comprimento(self):
        temp = self.cabeca
        counter = 0

        while (temp):
            counter += 1
            temp = temp.proximo
        return counter

    def maiores(self, n):
        temp = self.cabeca
        counter = 0

        while (temp):
            if(temp.dado > n):
                counter += 1
            temp = temp.proximo
        return counter

    def retornaCauda(self):
        temp = self.cabeca

        while temp.proximo:
            temp = temp.proximo
        return temp.dado

    def insereFim(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)

        if(self.cabeca == None):
            self.cabeca = novo_nodo
            return
        else:
            temp = self.cabeca
            while temp.proximo:
                temp = temp.proximo
            temp.proximo = novo_nodo

    def insere_no_inicio(self, novo_dado):
        novo_nodo = NodoLista(novo_dado)
        novo_nodo.proximo = self.cabeca
        self.cabeca = novo_nodo


lista = ListaEncadeada()

for i in range(8):
    lista.insere_no_inicio(i)
print("Lista:", lista)

# 2º retorna o número de nós com valor maior que N
print("\n2º Quant. de dados maiores que N é: ", lista.maiores(5))

# 3º retorna o número de nós com valor menor que N
print(" \n3º Retorna último dado do Node: ", lista.retornaCauda())

# 4º
lista.insereFim(2012)
print("\n4º Insere um elemento no final: ", lista)

# 1º Comprimento da Lista
print("\n1º Comprimento da Lista é: ", lista.comprimento())
