def ficha(nome = "<desconhecido>", gols=0):
    return nome, gols


def valida(nome, gols):
    n = g = ''
    if nome.strip() == '' and gols.strip() == '':
        n, g = ficha()
    else:
        if gols.strip() != '':
            validaGol = ['0','1','2','3','4','5','6','7','8','9']
            acertos = 0
            for i in range(0, len(gols)):
                for j in range(0, len(validaGol)):
                    if gols[i] == validaGol[j]:
                        acertos += 1
            if acertos == len(gols):
                gols = int(gols)
            else:
                gols = 0

        if nome.strip() == '':
            n, g = ficha(gols=gols)

        elif gols == '':
            n, g = ficha(nome=nome)

        else:
            validaGol = ['0','1','2','3','4','5','6','7','8','9']
            acertos = 0
            for i in range(0, len(gols)):
                for j in range(0, len(validaGol)):
                    if gols[i] == validaGol[j]:
                        acertos += 1

            if acertos == len(gols):
                gols = int(gols)
            else:
                gols = 0

            n, g = ficha(nome, gols)
    return n, g


nome = str(input('Nome do jogador: '))
gols = str(input(f'Quantos gols ele fez? '))

n, g = valida(nome, gols)

print(f"O jogador {n} fez {g} gol(s)")


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    tam = len(arr)
    pos = neg = zer = 0
    for i in arr:    
        if i == 0:
            zer += 1
        else:
            if i > 0:
                pos += 1
            else:
                neg += 1
    
    print(round(pos/tam, 6))
    print(round(neg/tam, 6))
    print(round(zer/tam, 6))
        
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
