rmin = 9**100
for n in range(1, 1000):

    a = bin(n)[2:]
    a += str(a.count('1') % 2)
    a += str(a.count('1') % 2)
    r = int(a, 2)
    if r < rmin and r > 253:
        rmin = r
        print(n)