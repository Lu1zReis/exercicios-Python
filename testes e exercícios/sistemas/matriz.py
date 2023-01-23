from ast import Return
from random import randint

matriz = [[], [], []]
nMatriz = []

def geraValores(m):
    for i in range(0, 3):
        for j in range(0, 3):
            val = randint(0, 9)
            while val in matriz[i]:
                val = randint(0, 9)
            matriz[i].append(val)

def somaMatriz(m):

    novoArray = [[], [], []]
    soma = 0

    for pos in range(0, 3): # esse laço que percorrerá toda a tabela

        for p in range(0, 3): # esse laço que irá em linha por vez
            soma = 0

            for l in range(0, 3): # esse laço somará as linhas
                soma += m[pos][l]

                if(l == 2): # quando tiver somado os valores, irá para a coluna

                    for c in range(0, 3): # esse laço percorrerá a coluna junto com a var p para pegar os valores de forma vertical

                        if m[pos][p] == m[c][p] and pos == c: # igualamos a var pos igual a var p para não só pegar o número, mas saber que é aquele valor mesmo, e não tirar mais de um valor na col por ser repetido
                            soma = soma + (m[c][p] - m[pos][p]) # tirando o valor igual

                        else:
                            soma += m[c][p]


            novoArray[pos].append(soma)

    return novoArray



geraValores(matriz)
print('Matriz antes:')
print(matriz[0])
print(matriz[1])
print(matriz[2], '\n')

nMatriz = somaMatriz(matriz)

print('Matriz somada:')
print(nMatriz[0])
print(nMatriz[1])
print(nMatriz[2])
