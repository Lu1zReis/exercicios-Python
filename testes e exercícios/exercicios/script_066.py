quant = soma = 0
while True:
    dado = int(input('Digite um valor (999 para parar): '))
    if dado == 999:
        break
    else:
        quant += 1
        soma += dado

print(f'A quantidade do(s) {quant} número(s) é {soma}!')
