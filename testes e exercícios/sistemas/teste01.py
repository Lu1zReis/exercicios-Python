import time
porc = ['.','.','.','.','.','.','.','.','.','.']
pos = val = 0
i = 0
while i < 10:
    porc[i] = '#'
    x = 0
    while x < 1:
        print(porc[i], end=' ')
        #time.sleep(1)
        x += 1 
    i += 1
# ir testando com numeros e sem o end='', para ir quebrando mesmo a linha
