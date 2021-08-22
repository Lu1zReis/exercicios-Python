palavras = ('palavra', 'estudar', 'aprender', 'jogar', 'animala')
ant_a = ant_e = ant_i = ant_o = ant_u = -1
for k in range(0, len(palavras)):

    a = palavras[k].count('a') 
    e = palavras[k].count('e')
    i = palavras[k].count('i')
    o = palavras[k].count('o')
    u = palavras[k].count('u')

    print('A palavra "{}" tem o "a" e o "e" na(s) posições: '.format(palavras[k]), end=' ')

    for j in range(0, len(palavras[k])):
 
        if e > 0:
            if palavras[k].index('e', j) != ant_e:
                print(palavras[k].index('e', j)+1, end=' ')
                e -= 1 
            ant_e = palavras[k].index('e', j)

    print('\n')

