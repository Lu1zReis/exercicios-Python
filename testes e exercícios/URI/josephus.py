"""
1 2 3 4 5 6
  x x x x x
"""

def retirar(valores_apagar, lista):
    aux = 0
    for c in valores_apagar:
        for k in lista:
            if c == k:
                print(lista.pop(k))
                lista.pop(k)
                aux += 1
    return lista

def josephus(n, k):
    ind = k - 1

    men = list(range(1, n+1))
    retira = list()
    while len(men) > 1:
        print(retira, men)
        retira.append(ind) # 3 6
        ind += k # 9

        if ind > len(men): # 9 > 6
            print(retira, men)
            men = retirar(retira, men)
            print(men)
            ind = ind - len(men) # 9 - 6
            retirar.clear()
            # nova lista: 1 2 3 4 5 6 -> 1 2 4 5
        
    print(men)

josephus(6,3)

"""
retirar = [3, 6]
men = list(range(1, 6))
print(men)
men = list(map(lambda x, i: men.pop(x), retirar))
print(men)

print(retirar([3,6], lista=list(range(1,6))))
"""