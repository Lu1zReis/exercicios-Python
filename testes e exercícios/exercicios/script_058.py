import random

Num_Pc = random.randint(0, 10)
print('-=-=-=-Descubra o número que eu (pc) escolhi-=-=-=-')
Num_Usu = Tentativas = 0

while Num_Pc != Num_Usu:
    Num_Usu = int(input('Adivinhe o número que o PC escolheu: '))
    Tentativas += 1

    if(Num_Usu < Num_Pc):
        print('Digite um valor maior...')
    if(Num_Usu > Num_Pc):
        print('Digite um valor menor...')


print('\nParabéns!! Você adivinhou o número que eu randomizei...\nEsse número que escolhi, como viu, foi o {} ^^'.format(Num_Pc))
print('Foram necessárias {} tentativa(s)\n'.format(Tentativas))

'''
Outro método...

acertou = False
while not acertou:
    Num_Usu = int(input())
    if Num_Usu == Num_Pc:
        acertou = True
    else:
        if(Num_Usu < Num_Pc):
            print('Digite um valor maior...')
        if(Num_Usu > Num_Pc):
            print('Digite um valor menor...')
'''
