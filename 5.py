for n in range(1, 13):

    a = bin(n)[2:]
    if n % 2 == 0:
        a =  '10' + a
    else:
        a = '1' + a + '01'

    r = int(a, 2)
    print(r, n)