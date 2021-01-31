contratados = int(input())
elfos = []
brinquedos = 0
Nome_elfo = ''
Prof_elfo = ''
Horas_elfo = 0
aux1 = 0
aux2 = 0
aux3 = 0
aux4 = 0

for c in range(0, contratados):
    Nome_elfo, Prof_elfo, Horas_elfo = input().split(' ')
    Nome_elfo = str(Nome_elfo)
    Prof_elfo = str(Prof_elfo).upper()
    Horas_elfo = int(Horas_elfo)

    elfos.append(Nome_elfo)
    elfos.append(Prof_elfo)
    elfos.append(Horas_elfo)


    if(elfos[1] == 'ARQUITETOS'):
        if(elfos[2] >= 4):
            brinquedos += 1
            aux1 += elfos[2] - (c * 4)
            if(aux1 >= 4):
                brinquedos += 1
    elif(elfos[1] == 'BONECOS'):
        if(elfos[2] >= 8):
            brinquedos += 1
            aux2 += elfos[2] - (c * 8)
            if(aux2 >= 8):
                brinquedos += 1
    elif(elfos[1] == 'MUSICOS'):
        if(elfos[2] >= 6):
            brinquedos += 1
            aux3 += elfos[2] - (c * 6)
            if(aux3 >= 4):
                brinquedos += 1
    else:
        if(elfos[2] >= 12):
            brinquedos += 1
            brinquedos += 1
            aux4 += elfos[2] - (c * 12)
            if(aux1 >= 12):
                brinquedos += 1

    elfos.clear()



print(brinquedos)
