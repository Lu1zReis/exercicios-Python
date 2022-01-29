valores = list()
pares = list()
impares = list()

for i in range(0, 7):
    val = int(input(f'Digite o {i+1}º valor: '))
    if val % 2 == 0:
        pares.append(val)
    else:
        impares.append(val)

valores.append(pares[:])
valores.append(impares[:])

print(sorted(valores[0]))
print(sorted(valores[1]))
