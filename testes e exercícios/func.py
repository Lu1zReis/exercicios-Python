a = str(input('Digite: '))
def temLetra_a(a):
    
    if('a' in a):
        return True
    else:
        return False

variavel = temLetra_a(a)

if variavel == True:
    print('tem letra A')
elif variavel == False:
    print('Não tem letra {}'.format(a))
else:
    print('...')

'''
testando outros módulos
'''

def funcao(x = 10, j = 0):
    i = x * j
    print(i)

c = int(input(': '))
u = int(input(': '))

funcao(c, u)
