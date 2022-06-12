tempo = []
horas = []
minut = []

SomTempo = 0
SomHoras = 0
SomMinut = 0

cont = 'S'

while 'S' in cont:
    tempo.append(float(input(': ')))
    cont = str(str(input('Deseja cont? '))).upper()

for i in range(0, len(tempo)):
    horas.append(int(tempo[i]))
    minut.append(round(tempo[i]-horas[i],2))

    SomHoras += horas[i]
    SomMinut += minut[i]

SomTempo = SomHoras + SomMinut

print(f'TEMPO ANTES: {SomTempo}')

while SomMinut >= 0.6:
    SomHoras += 1
    SomMinut -= 0.6

print('-='*30)

SomTempo = SomHoras + SomMinut
print(f'TEMPO DEPOIS: {SomTempo}')
