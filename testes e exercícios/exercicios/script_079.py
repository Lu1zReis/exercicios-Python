valores = list()
sair = 'n'
x = i = 0
while 's' not in sair:
    analise = 'erro'
    while 'acerto' not in analise:
        valores.append(int(input('Adicione um valor: ')))
        x = valores[i]
        if valores.count(x) > 1:
            print('Número existente, por favor adicione outro')
            valores.pop()
        else:
            print('Número adicionado com sucesso...')
            analise = 'acerto'
            i += 1
    sair = str(input('Deseja sair? ')).lower()
print(f'Você adicionou os seguintes valores: {sorted(valores)}')
