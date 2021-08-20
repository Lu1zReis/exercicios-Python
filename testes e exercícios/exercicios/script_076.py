lista = ('Pão', 1.50, 'Lápis', 2.10, 'Carne', 8.30, 'Lapiseira', 7.80)

preço = aux1 = aux2 = 0
produto = ''

print('-' * 30)
print('Listagem de preço')
print('-' * 30)

for pos in range(1, len(lista), 2):
    preço = lista[pos]
    for pos2 in range(aux1, 1):
        produto = lista[pos2+aux2]
    aux2 += 2
    print(f'{produto}......R$ {preço}')
