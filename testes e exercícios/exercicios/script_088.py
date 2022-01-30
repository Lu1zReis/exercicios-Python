import random
from tkinter import N
sorteados = list()
numeros = list()
v = 0
quant = int(input('Quantos jogos quer sortear? '))
print(f'SORTEANDO {quant} JOGOS')
k = 0
v = random.randint(0, 6)
numeros.append(v)
while len(numeros) < 6:
    for c in numeros:
        v = random.randint(0, 6)
        if v == c:
            v = random.randint(0, 6)
        numeros.append(v)
print(numeros)
