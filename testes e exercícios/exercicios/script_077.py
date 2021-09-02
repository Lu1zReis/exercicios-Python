palavras = ('palavra', 'estudar', 'aprender', 'jogar', 'animal', 'erro')

ant_a = ant_e = ant_i = ant_o = ant_u = -1
maior_a = maior_e = maior_i = maior_o = maior_u = 999
for k in range(0, len(palavras)):

    a = palavras[k].count('a') 
    e = palavras[k].count('e')
    i = palavras[k].count('i')
    o = palavras[k].count('o')
    u = palavras[k].count('u')

    print('A palavra "{}" tem as vogais nas posições em sequência da seguinte maneira: '.format(palavras[k]), end=' ')

    for j in range(0, len(palavras[k])):
        if a > 0:
            if palavras[k].index('a', j) != ant_a:
                maior_a = palavras[k].index('a', j)+1
                a -= 1 
            ant_a = palavras[k].index('a', j)

        if e > 0:
            if palavras[k].index('e', j) != ant_e:
                maior_e = palavras[k].index('e', j)+1
                e -= 1 
            ant_e = palavras[k].index('e', j)

        if i > 0:
            if palavras[k].index('i', j) != ant_i:
                maior_i = palavras[k].index('i', j)+1
                i -= 1 
            ant_i = palavras[k].index('i', j)

        if o > 0:
            if palavras[k].index('o', j) != ant_o:
                maior_o = palavras[k].index('o', j)+1
                o -= 1 
            ant_o = palavras[k].index('o', j)

        if u > 0:
            if palavras[k].index('u', j) != ant_u:
                maior_u = palavras[k].index('u', j)+1
                u -= 1 
            ant_u = palavras[k].index('u', j)

        vogais = (maior_a, maior_e, maior_i, maior_o, maior_u)

        for vogal in vogais:
            if maior_a < vogal:
                print('a', end=' ')
                maior_a = 999

            if maior_e < vogal:
                print('e', end=' ')
                maior_e = 999

            if maior_i < vogal:
                print('i', end=' ')
                maior_i = 999

            if maior_o < vogal:
                print('o', end=' ')
                maior_o = 999

            if maior_u < vogal:
                print('u', end=' ')
                maior_u = 999
    print('\n')
