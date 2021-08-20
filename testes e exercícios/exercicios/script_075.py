a = int(input('Digite um número: '))
b = int(input('Digite outro número: '))
c = int(input('Digite mais um número: '))
d = int(input('Digite o último número: '))

valor_par = quant9 = pos3 = 0

valores = (a, b, c, d)    

print(valores)
print(f'Quantidade de vezes que o valor 9 apareceram foram: {valores.count(9)}')

if valores.count(3):
    print(f'A posição que o valor 3 apareceu pela primeira vez foi a {valores.index(3)+1}º posição')
else:
    print('O valor 3 não foi digitado pelo usuário')

print('Os valores pares foram: ', end='')
for c in range(0, len(valores)):
    if valores[c] % 2 == 0:
        print(f'{valores[c]}', end=' ')

print('\n')
print('-=' * 10, end='')
print('Outra forma', end='')
print('-=' * 10)

for j in valores:
    if j == 9:
        quant9 += 1

for k in range(0, len(valores)):
    if valores[k] == 3:
        pos3 = k
        break
    else:
        pos3 = -1

print(f'A quantidade de vezes que o valor 9 apareceram foram: {quant9}')
if pos3 < 0:
    print('O valor 3 não aparece em nenhuma posição')
else:
    print(f'A posição que o valor 3 apareceu foi: posição {pos3+1}')
