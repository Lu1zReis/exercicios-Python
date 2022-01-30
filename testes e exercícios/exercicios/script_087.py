matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma3C = somaPar = maior2L = 0

for i in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite o valor [{i}][{c}]: '))
        matriz[i][c] = v
        
        # Pegando valores pares
        if v % 2 == 0:
            somaPar += v

        # Pegando o maior valor da 2a. linha
        if i == 1:
            if c == 0:
                maior2L = v
            else:
                if v > maior2L:
                    maior2L = v

print('------------Matriz------------')
for j in range(0, 3):
    print(f'[ {matriz[j][0]} ][ {matriz[j][1]} ][ {matriz[j][2]} ]')
    
    # Soma da 3ª coluna
    soma3C += matriz[j][2]

print('------------------------------')
print(f'A soma da 3ª coluna é: {soma3C}')
print(f'A soma dos pares é: {somaPar}')
print(f'O maior valor da 2ª linha é: {maior2L}')
