positivos = 0
Quant_positivos = 0
media = 0
for c in range(0, 6):
    valor = float(input())
    if(valor > 0):
        Quant_positivos += 1
        positivos += valor

media = positivos / Quant_positivos

print('{} valores positivos'.format(Quant_positivos))
print('{:.1f}'.format(media))
