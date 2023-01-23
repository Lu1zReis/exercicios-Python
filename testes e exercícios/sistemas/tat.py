def setTautogram():
    f = str(input()).split()
    return f

def getTautogram(v):
    tam = len(v)
    letra = ''
    erros = 0
    for i in range(0, tam):
        if i == 0:
            letra = v[i][0]
        else:
            if letra.lower() != v[i][0].lower():
                erros += 1
    if erros > 0:
        return 'N'
    else:
        return 'Y'

resul = list()

while True:
    frase = setTautogram()
    resul.append(getTautogram(frase))
    if '*' in frase:
        resul.pop()
        break

for r in resul:
    print(r)
