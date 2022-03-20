quadrante = ''
x = y = ''

while x != 0 and y != 0:

    x, y = input().split(' ')

    x = int(x)
    y = int(y)

    if x != 0 and y != 0:
        # quadrante 1:
        if x > 0:
            if y > 0:
                quadrante = 'primeiro'
            if y < 0:
                quadrante = 'quarto'

        if x < 0:
            if y > 0:
                quadrante = 'segundo'
            if y < 0:
                quadrante = 'terceiro'
    print(quadrante)

x = y = ''
quadr = ''
while x != 0 and y != 0:

    x, y = input().split(' ')
    x = int(x)
    y = int(y)

    if x != 0 and y != 0:
        if x > 0:
            if y > 0:
                quadr = 'primeiro'
            if y < 0:
                quadr = 'quarto'

        if x < 0:
            if y > 0:
                quadr = 'segundo'
            if y < 0:
                quadr = 'terceiro'

        print(quadr)
