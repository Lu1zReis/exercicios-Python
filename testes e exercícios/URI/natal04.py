n = int(input())
a, b, c = input().split(' ')
a = int(a)
b = int(b)
c = int(c)
maior = 0
iguais = 0
menor = 0
medio = 0
for k in range(0, n+1):
    if k == 0:
        maior = a
        medio = b
        menor = c
    else:
        if a == b:
            iguais = a
            maior = c
            menor = iguais
        elif a == c:
            iguais = c
            maior = b
            menor = iguais
        elif b == c:
            iguais = b
            maior = a
            menor = iguais

for c in range(0, n+1):
    if c > maior:
        maior = c
    elif b < menor:
        menor = b
    elif b > maior:
        maior = b
    elif a < menor:
        menor = a

for i in range(0, n+1):
    if a > menor and a < maior:
        medio = a
    elif b > menor and b < maior:
        medio = b
    elif c > menor and c < maior:
        medio = c


print('O maior valor: {}'.format(maior))
print('O valor medio: {}'.format(medio))
print('O menor valor: {}'.format(menor))
print('Há 2 valores com o valor: {}'.format(iguais))


# if iguais == maior:
#     print('Há dois valores iguais como maiores: {}'.format(iguais))
#     print('O menor número é: {}'.format(menor))
# elif iguais == menor:
#     print('Há dois valores iguais como menores: {}'.format(iguais))
#     print('O maior número é: {}'.format(maior))
# else:
#     print('O maior valor é: {}'.format(maior))
#     print('O menor valor é: {}'.format(menor))
