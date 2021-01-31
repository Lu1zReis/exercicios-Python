a1, a2, a3, a4, a5, a6 = input().split(' ')
a1 = int(a1)
a2 = int(a2)
a3 = int(a3)
a4 = int(a4)
a5 = int(a5)
a6 = int(a6)
i = 0
aux = 0
lista = [a1, a2, a3, a4, a5, a6]
for i in lista:
    if lista[i] >= 0:
        aux += 1
print('quantidade de positivos: {}'.format(aux))
