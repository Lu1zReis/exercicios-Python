matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for c in range(0, 3):
        v = int(input(f'Digite o valor [{i}][{c}]: '))
        matriz[i][c] = v

print('------------Matriz------------')
for j in range(0, 3):
    print(f'[ {matriz[j][0]} ][ {matriz[j][1]} ][ {matriz[j][2]} ]')
