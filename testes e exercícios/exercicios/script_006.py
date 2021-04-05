print('Aqui iremos pegar um valor e mostrar alguns resultados, como o\nDOBRO\nTRIPRO\nRAIZ QUADRADA')
valor = int(input('Informe um valor: '))
print('O dobro de {}, será {}'.format(valor, valor*2))
print('O triplo de {}, será {}'.format(valor, valor*3))
#Em números com bastantes casas decimais, se quisermos diminuir com {:.xf}
#x = qualquer número real
print('A raiz de {} quadrada será {:.2f}'.format(valor, valor**(1/2)))
