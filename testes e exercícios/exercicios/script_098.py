from time import sleep 

def contador(p1, p2, p3):

    # terceiro algoritmo (personalizado pelo usuário)
    inicio = p1
    fim = p2
    passo = p3

    if inicio > fim:
        if passo > 0:
            passo = passo - (passo * 2)
        if passo == 0:
            passo -= 1
    else:
        if passo == 0:
            passo = 1
        if passo < 0:
            passo *= -1
        

    for c in range(inicio, fim+passo, passo):
        if fim < inicio:
            if c >= fim:
                print(c, end=' ', flush=True)
                sleep(0.2)
        else:
            print(c, end=' ', flush=True)
            sleep(0.2)

    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)

print('=-' * 15)

ini = int(input('I: '))
fim = int(input('F: '))
pas = int(input('P: '))

contador(ini, fim, pas)
