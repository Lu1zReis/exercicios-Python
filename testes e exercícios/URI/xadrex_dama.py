valor = 0
x1, y1, x2, y2 = input().split(' ')

x1 = int(x1)
y1 = int(y1)
x2 = int(x2)
y2 = int(y2)

posX1 = x1 % 2
posY1 = y1 % 2
posX2 = x2 % 2
posY2 = y2 % 2

if 1 < x1 or x1 > 8 or 1 < y1 or y1 > 8 or 1 < x2 or x2 > 8 or 1 < y2 or y2 > 8:
    pass
else:
    if posX1 == 0 and posY1 == 0 and posX2 == 0 and posY2 == 0:
        valor = 1
    elif x1 == x2 and y1 == y2:
        valor = 0
    else:
        valor = 2

    print(valor)    
