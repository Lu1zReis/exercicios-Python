valores = list()
sair = 'n'
i = 0
while 's' not in sair:
    analise = 'erro'
    while 'acerto' not in analise:
        valores.append(int(input('Adicione um valor: ')))
        if valores.count(valores[i]) > 1:
            print('Número existente, por favor adicione outro')
            valores.pop()
        else:
            print('Número adicionado com sucesso...')
            analise = 'acerto'
            i += 1
    sair = str(input('Deseja sair? ')).lower()
print(f'Você adicionou os seguintes valores: {sorted(valores)}')
