from typing import Counter


lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim') # Tupla
print(lanche)

print('=' * 30)

print(lanche[1:4]) # Mesmo que não exista a posição 4, nesse fatiamento ele não pega a última extremidade, então vai pegar as posições: 1, 2 e 3
print(lanche[2:]) # Aqui ele vai da posição 2 até a posição final
print(lanche[:2]) # Aqui ele vai do inicio até a posição 1, pois ele não conta a extremidade final

print('=' * 30)

# Maneira de se exibir em for
for c in lanche:
    print(f'Maneira simples: {c}')
print('-'*10)
# Outra maneira de se exibir em for
for pos in range(0, len(lanche)):
    print(f'Maneira composta: {lanche[pos]} na posição {pos}º')
print('-'*10)
# Mais uma maneira
for cont, comida in enumerate(lanche):
    print(f'Vou comer {comida} na posição {cont}')

print('=' * 30)

# Mostrando de forma ordenado
print(sorted(lanche))

print('=' * 40)
# Outras características
a = (4, 2, 6)
b = (5, 4, 1, 3)
c = a + b 
print(c)
print(c.count(4)) # a função count conta quantas vezes aquele dado aparece
print(c.index(5)) # essa função index mostra a posição que o dado aparece
print(c.index(4, 1)) # essa função também pode receber 2 valores por parâmetro, o segundo sendo a partir da posição que queremos, ex: a partir da posição 1 comece a ver qual a posição do próximo 4

# Para deletar uma tupla, usamos del(variavel). Mas não podemos apagar só um dado de uma posição, ex: del(variavel[1]), isso não é possivel.
