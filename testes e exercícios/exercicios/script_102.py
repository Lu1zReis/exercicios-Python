def fatorial(n = 1, show = False):
    """
    fatorial(n, show = false)
    """
    f = 1
    for i in range(n, 0, -1):
        f *= i
        if show:
            print(i, end='')
            if i > 1:
                print(end=' x ')
            else:
                print(end=' = ', flush=False)
    return f

print(fatorial(5, show=True))
help(fatorial)