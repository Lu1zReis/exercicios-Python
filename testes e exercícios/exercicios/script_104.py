def leiaint(frase):
    """
    num = input(frase)

    vals = ['0','1','2','3','4','5','6','7','8','9']
    qnt = 0

    while qnt != len(num):
        for c in range(0, len(num)):
            if num[c] in vals:
                qnt += 1

        if qnt != len(num):
            qnt = 0
            print('ERRO! Digite um número válido.')
            num = input(frase)

    return num
    """
    # OUTRA FORMA DE FAZER ESSE CÓDIGO
    num = input(frase)
    while num.isnumeric() == False:
        print('\033[0;31mERRO! Digite um número válido\033[m')
        num = input(frase)
    return num

n = leiaint('digite um valor: ')
print(f'Você acabou de digitar {n}')
