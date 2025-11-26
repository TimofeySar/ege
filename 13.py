for A in range(1, 1000):
    for x in '0123456789ABCD':
        M = int('8' + x + '12' + x, 14)
        N = int('8' + x + '542', 14)
        if (M + A) % N == 0:
            print(A)
            exit()