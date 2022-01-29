dados = list()
cadastrados = list()
maisPes = []
menPes = []

while True:
    dados.append(str(input('Nome: ')))
    dados.append(str(input('Peso: ')))

    cadastrados.append(dados[:])

    dados.clear()

    sair = str(input('Deseja sair? '))
    if sair in 'sS':
        break

for pos, val in enumerate(cadastrados):
    if pos == 0:
        maisPes.append(val)
        menPes.append(val)
    else:
        if maisPes[0][1] < val[1]:
            maisPes.clear()
            maisPes.append(val[:])
        elif maisPes[0][1] == val[1]:
            maisPes.append(val[:])

        if menPes[0][1] > val[1]:
            menPes.clear()
            menPes.append(val[:])
        elif menPes[0][1] == val[1]:
            menPes.append(val[:])

print(f'Foram cadastrados {len(cadastrados)} valor(es)')
print(f'O(s) mais pesados: {maisPes}')
print(f'O(s) menos pesados: {menPes}')
