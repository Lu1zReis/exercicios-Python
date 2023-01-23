from time import sleep

def qntVezes(base):
    val = 0
    for i in range(1, base+1):
        if base % 2 == 0:
            if i % 2 == 0:
                val += 1
        else:
            if i % 2 == 1:
                val += 1
    return val


def piramide(base):
    k = base
    for i in range(1, base+1):
        # para centralizar a piramide
        if (base % 2 == i % 2) and (base % 1 == i % 1):
            # para ir empurrando para o meio
            print(' '* k, end='')

            for j in range(1, i+1):
                print("#", end='', flush='false')
                sleep(0.3)
            print()
            k-=1


def circulo(base):
    k = base
    for i in range(1, base+1):
        # para centralizar a piramide
        if (base % 2 == i % 2) and (base % 1 == i % 1):
            if qntVezes(base)-1 < i:

                # para ir empurrando para o meio
                print(' '* k, end='')

                for j in range(1, i+1):
                    print("*", end='', flush='false')
                    sleep(0.3)
                print()
                if i != base:
                    k-=1

    for i in range(1, base+1):
        # para centralizar a piramide
        if (base % 2 == i % 2) and (base % 1 == i % 1):
            if qntVezes(base)-1 < i:

                # para ir empurrando para o meio
                print(' '* k, end='')

                for j in range(base+1, 1, -1):
                    print("*", end='', flush='false')
                    sleep(0.3)
                print()
                if i != base:
                    k+=1
                

def main():
    # print(qntVezes(4))
    piramide(4)


main()
