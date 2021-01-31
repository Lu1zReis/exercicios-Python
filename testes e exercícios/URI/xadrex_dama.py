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

if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
    pass
else:
    if posX1 == 0 and posY1 == 0 and posX2 == 0 and posY2 == 0:
        valor = 1
    elif x1 == x2 and y1 == y2:
        valor = 0
    else:
        valor = 2

    print(valor)    
