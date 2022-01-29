lista = list()
maior = menor = 0
PosMaior = list()
PosMenor = list()
for i in range(0, 5):
    lista.append(int(input(f'Digite o {i+1}º valor: ')))

for pos, val in enumerate(lista):
    if pos == 0:
        maior = val
        menor = val
    else:
        if val > maior:
            maior =  val
        if val < menor:
            menor = val

for c, v in enumerate(lista):
    if v == maior:
        PosMaior.append(c)
    if v == menor:
        PosMenor.append(c)

print(f'Foram digitados os valores {lista}')
print(f'O maior número é {maior} As posições dele são: {PosMaior}')
print(f'O menor número é {menor} As posições dele são: {PosMenor}')
