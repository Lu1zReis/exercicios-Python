def notas(*provas, sit=False):
    sala = {'total': 0, 'maior': 0, 'menor': 0, 'media': 0}
    notas = 0
    i = 0
    for c in provas:
        sala['total'] += 1
        notas += c
        if i == 0:
            sala['maior'] = c
            sala['menor'] = c
            i += 1
        else:
            if c > sala['maior']:
                sala['maior'] = c
            if c < sala['menor']:
                sala['menor'] = c

    sala['media'] = notas / sala['total']  

    if sit == True:
        if sala['media'] < 6:
            sala['situacao'] = "RUIM"
        else:
            if sala['media'] >= 6 and sala['media'] < 7:
                sala['situacao'] = "RAZOAVEL"
            else:
                sala['situacao'] = "BOA"

    return sala

print(notas(5,7.4,8.5, sit=True))
