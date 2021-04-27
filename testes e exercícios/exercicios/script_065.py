parar = 'S'
num = quant = media = maior = menor = soma = 0
while parar in 'S':
    num = int(input('Digite um valor: '))

    # Atribuindo os valores
    quant += 1
    soma += num
    if quant == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    parar = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

media = soma / quant

print('Você digitou {} número(s) e a media foi {}'.format(quant, media))
print('O maior valor foi {} e o menor valor foi {}'.format(maior, menor))
