def tempoConversao(s):
    
    meioTempo = s[-2] + s[-1]

    val = int(s[0]+s[1])
    s_nova = ""
    if meioTempo == "PM":
        if val == 12:
            s_nova = s
        else:
            val = 12 + int(s[0] + s[1])
            s_nova = str(val)
            for c in range(0,len(s)):
                if c > 1:
                    
                    if c != len(s)-1 and c != len(s)-2:
                        s_nova += s[c]

    if meioTempo == "AM":
        if val == 12:
            for c in range(0, len(s)):
                if c == 0 or c == 1:
                    s_nova += '0'
                else:
                    if c != len(s)-1 and c != len(s)-2:
                        s_nova += s[c]
        else:
            for c in range(0,len(s)):
                
                if c != len(s)-1 and c != len(s)-2:
                    s_nova += s[c]
        
    
    print(s_nova)
    
    "CODI 2"
    """
    
    meioTempo = s[-2:] # pegando as pos finais

    val = int(s[:2])
    s_nova = ""
    
    if meioTempo == "PM":
        if val == 12:
            s_nova = s.replace('PM', '')
        else:
            val = 12 + val
            s_nova = str(val)
            s = s.replace(s[:2], s_nova)
            s_nova = s.replace(s[-2:], "")

    if meioTempo == "AM":
        if val == 12:
            s_nova = s.replace('12', '00')
            s_nova = s.replace('AM', '')
        else:
            s_nova = s.replace('AM', '')

    """
    
    "COD 3"
    """
    from datetime import datetime
    time = datetime.strptime(s, '%I:%M:%S%p')
    return time.strftime('%H:%M:%S')
    """        

tempoConversao('01:05:45PM')
