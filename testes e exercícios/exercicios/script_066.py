idade = Maior18 = quantHomens = MulhMenos20 = cont = 0
while True:
    print('\n---CADASTRE UMA NOVA PESSOA---\n')

    idade = int(input('Digite a sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o seu sexo: [M/F] ')).strip().upper()[0]

    if sexo == 'M':
        quantHomens += 1
        if idade >= 18:
            Maior18 += 1
    elif sexo == 'F':
        if idade < 20:
            MulhMenos20 += 1
        elif idade >= 18:
            Maior18 += 1

    cont += 1
    sair = ' '

    while sair not in 'SN':
        sair = str(input('Deseja continuar cadastrando? [S/N]: ')).strip().upper()[0]

    if 'N' in sair:
        break
    
print('-=-' * 20)
print(f'Ao total foram cadastradas {cont} pessoa(s) e há {Maior18} maior(es) de 18 anos')
print(f'Ao total de homens cadastrados, foram {quantHomens}')
print(f'Há {MulhMenos20} mulher(es) com menos de 20 anos')
