# EXERCÍCIO PARA PRÁTICA

1. Modifique o programa 6.8 (presente no material de estudos sobre pilhas), para que ele tenha duas funções:
 - [x] 1. empilhar - push(item)
 - [x] 2. desempilhar - pop()


2. Modifique o programa resultante da questão 1 para que o item a ser empilhado seja informado pelo usuário. Indique na saída do programa quando o item for desempilhado.

**Exemplo de execução do programa:**
Pilha atual: [1, 2, 3, 4, 5]
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S):E
Qual elemento deseja empilhar? 15

Pilha atual: [1, 2, 3, 4, 5, '15']
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S):E
Qual elemento deseja empilhar?Estrutura de dados

Pilha atual: [1, 2, 3, 4, 5, '15', 'Estrutura de dados']
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S): E
Qual elemento deseja empilhar? 8.5

Pilha atual: [1, 2, 3, 4, 5, '15', 'Estrutura de dados', '8.5']
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S):D
8.5 desempilhado.

Pilha atual: [1, 2, 3, 4, 5, '15', 'Estrutura de dados']
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S):D
Estrutura de dados desempilhado.

Pilha atual: [1, 2, 3, 4, 5, '15']
Digite E para empilhar um novo elemento,
ou D para desempilhar. S para sair.
Operação (E, D ou S):S



3. Utilizando uma pilha (vc pode utilizar as funções para pilha criadas nas questões 1 e 2), crie um programa que verifica se as expressões contendo parênteses estão corretas ou incorretas.

**Exemplo de execução do programa:**
- ()() - CORRETO
- (() - INCORRETO
- )( - INCORRETO
- () - CORRETO
