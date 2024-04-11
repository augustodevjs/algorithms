def reorganizarpilha(pilha):
    fila = []
    pilha_esquerda = [] 
    pilha_direita = [] 
    
    tamanho = len(pilha)

    if tamanho <= 1:
        return pilha

    meio = tamanho // 2

    for i in range(tamanho):
        if i < meio:
            pilha_esquerda.append(pilha.pop())
        else:
            pilha_direita.append(pilha.pop())

    while pilha_esquerda and pilha_direita:
        fila.append(pilha_direita.pop())
        fila.append(pilha_esquerda.pop())

    return fila

x = [4, 3, 2, 5] 
fila = reorganizarpilha(x)

for elemento in fila:
    print(elemento, end=" ")
