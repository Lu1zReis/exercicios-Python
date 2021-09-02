h1, m1, h2, m2 = input(': ').split(' ')
convertH = convertH2 = resu = 0
h1 = int(h1)
m1 = int(m1)
h2 = int(h2)
m2 = int(m2)

if h1 < 0 or h1 > 23 and h2 < 0 or h2 > 23:
    pass
elif m1 < 0 and m1 > 23 and m2 < 0 and m2 > 23:
    pass
elif h1 == h2:
    print('As horas são iguais')
    resu = (h2 * 60) + (m1 - m2)
"""
        else:
            if m1 > m2:

    else:
        convertH = (60 * h1) + m1
        convertH2 = (60 * h2) + m2
        resu = convertH2 - convertH
"""
print(resu)
