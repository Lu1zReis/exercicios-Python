def notas(*provas, sit=False):
    """
    
    """
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

    # PODERIAMOS FAZER TAMBEM DA SEGUINTE FORMA
    """
    sala['total'] = len(provas)
    sala['maior'] = max(provas)
    sala['menor'] = min(provas)
    sala['media'] = sum(provas)/len(provas)
    if sit:
        if sala['media'] >= 7:
            sala['situacao'] = "BOA"
        elif sala['media'] >= 5:
            sala['situacao'] = "RAZOAVEL"
        else:
            sala['situacao'] = "RUIM"
    """
    return sala


print(notas(5,7.4,8.5, sit=True))
