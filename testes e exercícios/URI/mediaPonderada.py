n = int(input())
ValorF = 0
resuF = []

for i in range(0, n):
    resu = 0
    a, b, c = input().split(' ')

    a = float(a)
    b = float(b)
    c = float(c)

    resu += a * 2
    resu += b * 3
    resu += c * 5
    
    resu /= 10
    resuF.append(resu)

size = len(resuF)

for k in range(0, size):
    ValorF = resuF[k]
    print(f'{ValorF:.1f}')
