def valor100():
    valorInicial = int(input())
    valor = valorInicial // 100
    print('{} nota(s) de R$ 100,00'.format(valor))
    nota50 = valorInicial - (valor * 100) 
    return nota50

def valor50():
    valorInicial = valor100()
    valor = valorInicial // 50
    print('{} nota(s) de R$ 50,00'.format(valor))
    nota20 = valorInicial - (valor * 50) 
    return nota20

def valor20():
    valorInicial = valor50()
    valor = valorInicial // 20
    print('{} nota(s) de R$ 20,00'.format(valor))
    nota10 = valorInicial - (valor * 20) 
    return nota10

def valor10():
    valorInicial = valor20()
    valor = valorInicial // 10
    print('{} nota(s) de R$ 10,00'.format(valor))
    nota5 = valorInicial - (valor * 10) 
    return nota5

def valor5():
    valorInicial = valor10()
    valor = valorInicial // 5
    print('{} nota(s) de R$ 5,00'.format(valor))
    nota2 = valorInicial - (valor * 5) 
    return nota2

def valor2():
    valorInicial = valor5()
    valor = valorInicial // 2
    print('{} nota(s) de R$ 2,00'.format(valor))
    nota1 = valorInicial - (valor * 2) 
    return nota1

def valor1():
    valorInicial = valor2()
    valor = valorInicial // 1
    print('{} nota(s) de R$ 1,00'.format(valor))
    nota = valorInicial - (valor * 1) 
    return nota

valor1()