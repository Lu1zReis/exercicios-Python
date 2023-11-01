def data():
    aux=['A B C D E F G H I J K L M N O P']
    A =  '0 1 1 1 0 0 0 0 0 1 0 1 0 0 1 0'
    B =  '0 1 1 1 1 0 0 0 0 1 0 1 0 0 1 0'
    C =  '0 1 0 0 1 0 0 0 0 0 0 1 0 0 1 0'
    D =  '0 1 1 1 1 0 0 0 0 0 0 1 0 0 1 0'
    E =  '0 1 0 0 1 0 0 0 0 1 0 1 0 0 1 0'
    F =  '0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0'
    G =  '1 1 0 1 1 1 1 1 0 1 0 0 0 0 0 0'
    H =  '0 0 1 1 0 0 0 0 0 1 0 1 0 0 1 0'
    I =  '0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0'
    J =  '0 0 1 1 1 0 0 0 0 0 0 0 0 0 1 0'
    K =  '0 0 0 0 0 0 0 0 0 0 0 1 1 0 1 1'
    L =  '0 0 0 0 1 0 0 0 0 0 0 1 0 0 1 0'
    M =  ''

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

def showTables():
    k = 1
    print('  ABCDE   A B C D E F G H I J K L M N O P')
    for i in range (65, 91):
        print (chr(i), end=" ")
        if (k == 1):
              print ('0000',end='')
        elif (k > 1 and k < 4):
            print('000', end='')
        elif (k > 3 and k < 8):
            print('00', end='')
        elif (k > 7 and k < 16):
            print('0',end='')
        print (format(k, "b"))
        k+=1

showDisplay()
showTables()

