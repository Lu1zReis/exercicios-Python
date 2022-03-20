
# Variaveis:
x, y = input().split(' ')
x = int(x)
y = int(y)

val = val2 = val3 = 0

BinX = list()
BinY = list()

BinL = list()
Ordem = list()
bin = list()

OrdemX = []
OrdemY = []
# essa var bin se usa no código para fazer a soma de tudo no fim
bin1 = []
bin2 = []

# coletando os dados e transformando de decimal para binario
def Dados(x):
    lista = list()
    while x != 0:
        if x % 2 == 0:
            lista.append(0)
        if x % 2 != 0:
            lista.append(1)
        x = x // 2

    # colocando mais 0 se a lista não tiver os 3 valores
    while len(lista) < 3:
        lista.append(0)
    return lista

BinX = Dados(x)
BinY = Dados(y)

def soma():
    maior = 0
    if len(BinY) > len(BinX):
        maior = len(BinY)
        while len(BinX) < len(BinY):
            BinX.append(0)
    elif len(BinY) < len(BinX):
        maior = len(BinX)
        while len(BinX) < len(BinY):
            BinY.append(0)
    else:
        maior = len(BinX)
    
    for j in range(0, maior):
        if BinX[j] + BinY[j] == 1:
            BinL.append(1)
        elif BinX[j] + BinY[j] == 2:
            BinL.append(0)
        else:
            BinL.append(0)

def ordem():
    # ajustando em ordem correta
    for i in range(len(BinX)-1, -1, -1):
        OrdemX.append(BinX[i])
        bin1.append(BinX[i]*(2**i))
    # ajustando em ordem correta
    for i in range(len(BinY)-1, -1, -1):
        OrdemY.append(BinY[i])
        bin2.append(BinY[i]*(2**i))

    for i in range(len(BinL)-1, -1, -1):
        Ordem.append(BinL[i])
        bin.append(BinL[i]*(2**i))

def transf(val, val2, val3):

    # transformando de binario para decimal
    for j in range(0, len(BinX)):
        val += bin1[j]

    # transformando de binario para decimal
    for j in range(0, len(BinY)):
        val2 += bin2[j]

    # transformando de binario para decimal
    for j in range(0, len(BinL)):
        val3 += bin[j]
        
    return val, val2, val3


Dados(x)
Dados(y)
soma()
ordem()

print(transf(val, val2, val3)[2])

