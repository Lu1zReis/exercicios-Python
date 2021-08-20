import random

w = random.randint(0, 20)
x = random.randint(0, 20)
y = random.randint(0, 20)
z = random.randint(0, 20)

maior = menor = 0
valores = (w, x, y, z)

print(f'Os valores gerados foram: {valores}')

for c in range(0, len(valores)):
    if c == 0:
        maior = valores[c]
        menor = valores[c]
    else:
        if valores[c] > maior:
            maior = valores[c]
        if valores[c] < menor:
            menor = valores[c]

print(f'O maior valor dessa tupla é: {maior}')
print(f'O menor valor dessa tupla é: {menor}')
