valor = maior = pos = 0

for i in range(0, 100):
    valor = int(input())
    if i == 0:
        maior = valor
    else:
        if valor > maior:
            maior = valor
            pos = i+1

print(maior)
print(pos)
