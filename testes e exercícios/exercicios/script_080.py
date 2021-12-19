lista = list()

for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    # print(f'O valor {lista[i]} foi adicionado na posição:', end=' ')
    pos = 0
    for n in range(0, len(lista)):
        if lista[0] > lista[n]:
            aux = lista[n]
            aux2 = lista[0]
            lista.pop(n)
            lista.pop(0)
            lista.insert(0, aux)
            lista.insert(1, aux2)

        if lista[n-1] > lista[n]:
            aux = lista[n]
            aux2 = lista[n-1]
            lista.pop(n)
            lista.pop(n-1)
            lista.insert(n-1, aux)
            lista.insert(n, aux2)
        print(lista)

 
print(lista)
