quant = 0
while True:
    quant += 1
    if quant == 1:
        nome = Nome_Barato = ''
        preço = total = mais1000 = barato = 0
    cont = ''

    nome = str(input('Digite o nome do produto comprado: '))
    preço = float(input('Digite o preço desse produto R$: '))

    total += preço
    if preço >= 1000:
        mais1000 += 1
    if quant == 1 or preço < barato:
        barato = preço
        Nome_Barato = nome

    while cont != 'S' and cont != 'N':
        cont = str(input('Deseja continuar? [S/N] ')).upper()[0]
    if cont == 'N':
        print(f'O total gasto é de R${total:.2f}')
        print(f'A quantidade de produtos que custam mais de R$1000 são {mais1000}')
        print(f'O produto mais barato é {Nome_Barato} que custa R${barato:.2f}')
        break
