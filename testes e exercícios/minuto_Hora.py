HoraI, MinuI, HoraF, MinuF = input().split(' ')

HoraI = int(HoraI)
MinuI = int(MinuI)
HoraF = int(HoraF)
MinuF = int(MinuF)

if(HoraI < HoraF):
    duracao = HoraF - HoraI
if(HoraI > HoraF):
    duracao = (24 - HoraI) + HoraF
if(HoraI == HoraF):
    duracao = 24

if(MinuI < MinuF):
    duracaoM = MinuF - MinuI
if(MinuI > MinuF):
    duracaoM = (60 - MinuI) + MinuF
if(MinuI == MinuF):
    duracaoM = 0

if(duracaoM >= 59):
    duracao = duracao - 1


print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(duracao, duracaoM))
