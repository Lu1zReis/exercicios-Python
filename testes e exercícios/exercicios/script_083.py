validar = list()
val1 = val2 = 0
validar = input('Digite a expressão: ').split(')')
for pos, num in enumerate(validar):
    if '(' in validar[pos]:
        val1 += validar[pos].count('(')
    if validar[pos] == '' or ')' not in validar[pos]:
        if '(' not in validar[pos]:
            val2 += 1
            if val2 > 0  and val1 == 0:
                val1 = 0
                break 
print(f'Lista = {validar}')
print('Expressão Válida!' if val1 == val2 else 'Expressão Incorreta!')
