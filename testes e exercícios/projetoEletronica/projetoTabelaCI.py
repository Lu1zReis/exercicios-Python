def data():
    #a =['A B C D E F G H I J K L M N O P']
    esp ='0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
    A =  '0 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0'
    B =  '0 1 1 1 1 0 0 0 0 1 0 1 0 0 1 0'
    C =  '0 1 0 0 1 0 0 0 0 0 0 1 0 0 1 0'
    D =  '0 0 1 1 1 0 0 0 0 1 0 0 0 0 1 0'
    E =  '0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0'
    F =  '0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0'
    G =  '1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0'
    H =  '0 0 1 1 0 0 0 0 0 1 0 1 0 0 1 0'
    I =  '0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0'
    J =  '0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 0'
    K =  '0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 1'
    L =  '0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 0'
    M =  '0 0 1 1 0 0 1 1 0 0 1 0 1 0 0 0'
    N =  '0 0 1 1 0 0 1 1 0 0 1 0 0 0 0 1'
    O =  '0 1 1 1 1 0 0 0 0 0 0 1 0 0 1 0'
    P =  '0 1 1 0 0 0 0 0 0 0 0 1 0 0 1 0'
    Q =  '0 1 1 1 0 0 0 0 0 1 0 1 0 0 0 0'
    R =  '0 1 1 0 0 0 0 0 0 1 0 1 0 0 1 1'
    S =  '0 1 0 1 1 0 0 0 0 1 0 1 0 0 0 0'
    T =  '1 1 0 0 0 0 0 0 0 0 0 1 0 0 1 0'
    U =  '0 0 1 1 1 0 0 0 0 0 0 1 0 0 1 0'
    V =  '0 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0'
    W =  '0 0 1 1 0 0 1 1 0 0 0 0 0 1 0 1'
    X =  '0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 1'
    Y =  '0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0'
    Z =  '1 1 0 0 1 1 0 0 0 0 0 0 1 1 0 0'
    return [esp,A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z]

def showDisplay():
    print("     A      B  ")
    print("  ------ ------")
    print("H | \K  |L  /M | C")
    print("  |  \  |  /   |  ")
    print("  ---I-- --J---   ")
    print("G |  N/ |  \P  | D")
    print("  |  /  |O  \  |  ")
    print("  ------ ------ ")
    print("     F     E   ")

def karnaugh(pos):
    if pos == 1: pos=0
    column = ['000','001','011','010','110','111','101','100']
    lines  = ['00','01','11','10']
    values = data()      
    val = {}
    k = 0
    for i in range (65, 92):
        a = ''
        if (k <= 1):
            a = '0000'
        elif (k > 1 and k < 4):
            a = '000'
        elif (k > 3 and k < 8):
            a = '00'
        elif (k > 7 and k < 16):
            a = '0'
        val[a+format(k,'b')] = values[k][pos]
        k+=1
    print("", end="  ")
    for j in column:
        print(j,end=" ")
    print()
    for p in range(len(lines)):
        print(lines[p], end=" ")
        for q in range(len(column)):
            if (lines[p]+column[q] in val):
                print(val[lines[p]+column[q]],end="   ")
            else:
                print("x", end="   ")
        print()


def showTables():
    k = 1
    dis = data()
    print('  ABCDE   A B C D E F G H I J K L M N O P')
    print('-----------------------------------------')
    print('_ 00000', end="   ")
    print(dis[0])
    for i in range (65, 91):
        print (chr(i), end=" ")
        a = ''
        if (k == 1):
            a = '0000'
        elif (k > 1 and k < 4):
            a = '000'
        elif (k > 3 and k < 8):
            a = '00'
        elif (k > 7 and k < 16):
            a = '0'
        print (a + str(format(k, "b")),end="   ")
        print(dis[k])
        k+=1

yes = True
showDisplay()
showTables()
while yes:
    c = int(input("Wich column do u wanna get?: "))
    print("Showing column ", chr(c+64))
    karnaugh(c)
    r = str(input("Would u to continue? [Y/N]: ")).upper()
    if r == 'N': yes = False 
