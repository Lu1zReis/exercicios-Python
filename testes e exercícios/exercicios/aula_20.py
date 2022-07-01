# aula de funções
""" 
    Definir funções são importantes em um código, já que, com elas,
    definimos uma rotina que se torna frequente, assim então podemos 
    reutilizar um trecho de código de uma maneira mais técnica e 
    limpa para o programa. 
"""
# função sem parâmetro
def lin():
    print('-' * 20)

# função com parâmetro
def soma(a, b):
    s = a + b
    print(f"A soma do valor a({a}) + b({b}) = s({s});")


# quando chamamos uma função, ela retorna no topo do programa, executa o código e depois continua o programa:
lin()
soma(2, 6)
lin()
# podemos passar um valor definido
soma(b=2, a=1)

# podemos usar o empacotamento de parâmetro usando o '*'
def valores(*num):
    print(num)

lin()
valores(1, 2, 3)
valores(3, 6, 5, 1)

lin()
# ou podemos usar esse empacotamento com listas
def dobra(lst):
    for i in range(0, len(lst)):
        lst[i] *= 2

vals = [1, 2, 3, 4]
print(f'lista anterior: {vals}')
dobra(vals)
print(f'lista depois: {vals}')
