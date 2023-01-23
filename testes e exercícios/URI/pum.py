n = int(input())
cont = 1

for i in range(0, n):
    for j in range(0, 4):
        if j == 3:
            print('PUM')
        else:
            print(cont, end=' ')
        cont += 1
