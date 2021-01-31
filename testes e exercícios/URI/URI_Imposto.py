entrada = float(input())

def definir_imposto(entrada): # Precisamos definir que essa função vai receber a "entrada" para ser usada mais vezes
    if entrada <= 2000.00:
        return False
    elif entrada > 2000.00 and entrada <= 3000.00:
        a = (entrada - 2000) * 0.08
        return a
    elif entrada > 3000.00 and entrada <= 4500.00:
        a = ((entrada - 3000) * 0.18) + 80
        return a
    else:
        a = (((entrada - 4500) * 0.28) + 80) + 270
        return a

i = definir_imposto(entrada)
if i == False:
    print('Isento')
else:
    print('R$ {:.2f}'.format(i))
