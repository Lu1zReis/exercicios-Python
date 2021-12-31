lista = []
pares = []
impares = []
continuar = 's'
while 'n' not in continuar:
    lista.append(int(input('Adicione um valor: ')))
    continuar = str(input('continuar [S/N]: '))
for r in range(0, len(lista)):
    if lista[r] % 2 == 0:
        pares.append(lista[r])
    else:
        impares.append(lista[r])
print(f'Lista: {lista}')
print(f'Pares: {pares}')
print(f'Ímpares: {impares}')
