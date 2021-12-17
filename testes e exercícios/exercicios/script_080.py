lista = list()
for i in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
    while lista[i-1] > lista[i]:
        lista.insert(i-1, lista[i])
        lista.pop()

print(lista)
