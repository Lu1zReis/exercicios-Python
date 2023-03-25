tam = int(input('Digite a ordem da matriz: '))
matrizOrigem = list()
matriz = []
vals = []

for l in range(0, tam):
    for c in range(0, tam):
        vals.append(float(input(f'[{l}][{c}]:')))

    # aqui colocamos 0 e 1 na matriz inversa que iremos trabalhar, fazendo isso o usuário não precisará digitar muito
    for aux in range(0, tam):
        if aux == l:
            vals.append(1)
            print(1)
        else:
            vals.append(0)
            print(0)

    print()
    matrizOrigem.append(vals[:])
    matriz.append(vals[:])
    vals.clear()

# quando há tam*2 em alguns trecho do código significa que os valores que trabalharemos na matriz principal tamvém afetarão a matriz inversa 
print(matriz)
def pivos(l, c):
    print(f'\nAchando PIVO da linha: {l}')
    pivo = matriz[l][c]
    print(f'{matriz}')
    for j in range(0, tam*2):
        # criando essa cond para não dar o erro de float sendo dividido quando é 0
        if pivo != 0:
            print(f'{matriz[l][j]}*=1/{pivo}',end=' = ')
            matriz[l][j] = round(matriz[l][j] * (1/pivo), 4) 
        print(f'{matriz[l][j]}\n')


def zerar(l):
    print(f'\nzerando ABAIXO/ACIMA da linha: {l}')
    for k in range(0, tam):
        aux = 0
        for i in range(0, tam*2):
            if l == i:
                aux = matriz[k][i]

            if k != l:
                print(f'{matriz[k][i]}-={aux}*{matriz[l][i]}',end=' = ')
                matriz[k][i] = round(matriz[k][i]-(aux*matriz[l][i]), 4)
                print(f'{matriz[k][i]}\n')


# não colocamos o a matriz inversa aqui para ser percorrida aqui porque não queremos que o resultado faça parte da matriz, e sim que seja um valor a parte  
for l in range(0, tam):
    for c in range(0, tam):
        if l == c:
            pivos(l, c)
            zerar(l) 


print()

for lin in range(0, tam):
    for col in range(0, tam*2):
        if col == tam:
            print("|", end="")
        if col >= tam:
            matriz[lin][col] = round(matriz[lin][col],2)
            if matriz[lin][col] == -0.00:
                print(f'0.0', end=", ")
            else:
                print(f'{matriz[lin][col]}', end=", ")
        else:
            if matriz[lin][col] == -0.0:
                print(0, end=', ')
            else:
                print(f'{matriz[lin][col]:.0f}', end=', ')
    print()
