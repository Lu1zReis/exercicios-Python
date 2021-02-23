<<<<<<< HEAD
quant = 0
size = 0
for c in range(1, 500):
    valor = 3 * c
    if valor % 2 == 1:
        quant += 1
        size += valor
        if 3 * c >= 495:
            break
print('A quantidade foi: {}, e ao todo ficou {}'.format(quant, size))

# Outra forma

soma = 0
cont = 0
for c in range(1, 500, 2):
    if(c % 3 == 0):
        cont += 1
        soma += c
=======
quant = 0
size = 0
for c in range(1, 500):
    valor = 3 * c
    if valor % 2 == 1:
        quant += 1
        size += valor
        if 3 * c >= 495:
            break
print('A quantidade foi: {}, e ao todo ficou {}'.format(quant, size))

# Outra forma

soma = 0
cont = 0
for c in range(1, 500, 2):
    if(c % 3 == 0):
        cont += 1
        soma += c
>>>>>>> 740019a2dbb68d18689863dbaf0110e4f2edcc99
print('\nA quantidade foi: {}, e ao todo ficou {}'.format(cont, soma))