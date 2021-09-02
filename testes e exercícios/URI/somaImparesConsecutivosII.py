valores = []
quant = int(input())
for c in range(0, quant):
    x, y = input().split(' ')
    x = int(x)
    y = int(y)
    maior = menor = soma = 0
    if x > y:
        maior = x
        menor = y

    else:
        maior = y
        menor = x
    if maior == menor+1 or maior == menor:
        valores.append(0)
    else:
        for i in range(menor+1, maior):
            if i % 2 != 0:
                soma += i
            if i+1 == maior:
                valores.append(soma)
for valor in valores:
    print(valor)
