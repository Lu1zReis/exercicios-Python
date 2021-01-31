mult = float(input('Digite o valor a ser multiplicado: '))
x = 0
inicio = 0
aux = mult
valor_Inicial = x

while inicio < 20:
    inicio += 1

    x += 1
    calc = x * mult
    valor = calc - x

    if(valor == 9):
        print('O valor é: {}'.format(x))
    
    else:
        if(inicio == 20):
            print('Não tem uma razão aqui')
    pass
