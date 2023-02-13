def quebraRecorde(pontos):
    miniMaxi = [0,0]
    maxi = mini = 0
    # linhas comentados são para printar os valores em forma de tabela
    # print(f' game    pontos    minimo    maximo    min    max')
    for ind, val in enumerate(pontos):
        if ind == 0:
            maxi = val
            mini = val
            # print(f'{ind:^6}{val:>7}{mini:>10}{maxi:>10}{miniMaxi[0]:>8}{miniMaxi[1]:>7}')
        else:
            if val > maxi:
                maxi = val
                miniMaxi[1] += 1
            if val < mini:
                mini = val
                miniMaxi[0] += 1
            # print(f'{ind:^6}{val:>7}{mini:>10}{maxi:>10}{miniMaxi[0]:>8}{miniMaxi[1]:>7}')
    
    return miniMaxi

pontos = [12, 24, 10, 24]
recordes = quebraRecorde(pontos)
print(recordes)
