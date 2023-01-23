def tempoConversao(s):
    # descobrindo se é PM ou AM
    meioTempo = s[-2] + s[-1]
    horasInternacional = list(range(1, 13))
    
    horasLocal = list(range(0, 24))
    val = int(s[0]+s[1])

    if meioTempo == "PM":
        if val == 12:
            s[0] = '1'
            s[1] = '2'
        else:
            val = 12 + int(s[0] + s[1])
            s2 = str(val)
            print(s2)
            s[0] = s2[0]
            s[1] = s2[1]
           
    print(s)
        

tempoConversao('07:05:45PM')
