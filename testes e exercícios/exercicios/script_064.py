entrada = cont = quant = 0

while entrada != 999:
    entrada = int(input('Digite um valor [999 para parar]: '))
    if entrada != 999:
        quant += entrada
        cont += 1

print('Foram {} digitos e a soma entre eles foi {}'.format(cont, quant))
