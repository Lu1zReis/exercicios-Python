HoraI, MinI, HoraF, MinF = input().split(' ')

HoraI = int(HoraI)
MinI = int(MinI)
HoraF = int(HoraF)
MinF = int(MinF)
HoraT = 0
MinT = 0

if HoraI == HoraF:
    if MinI == MinF:
        HoraT = 24
    else:
        if MinF > MinI:
            MinT = MinF - MinI
        else:
            MinT = 60 - (MinF - MinI)
            HoraT -= 1
else:
    if HoraI > HoraF:
        HoraT = HoraF - HoraI
        if MinF > MinI:
            MinT = MinF - MinI
        else:
            MinT = 60 - (MinF - MinI)
            HoraT -= 1