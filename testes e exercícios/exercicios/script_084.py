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
if(len(maisPes) == 1):
    print(f'O mais pesado: {maisPes[0][1]} kg. de {maisPes[0][0]}')
else:
    i = 0
    print(f'Os mais pesados: {maisPes[0][1]} kg. de', end=' ')
    while i < len(maisPes):
        print(maisPes[i][0], end=' ')
        i+=1
if(len(menPes) == 1):
    print(f'O menos pesado: {menPes[0][1]} kg. de {menPes[0][0]}')
else:
    i = 0
    print(f'Os menos pesados: {menPes[0][1]} kg. de', end=' ')
    while i < len(menPes):
        print(menPes[i][0], end=' ')
        i+=1
