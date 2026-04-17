def dell(n):
    m = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            m.append(i)
            m.append(n // i)
    return len(set(m))

from fnmatch import fnmatch
for i in range(10**8, 2 * 10 ** 8):
    if fnmatch(str(i), '?*34*49'):
        if dell(i) == 1:
            print(i)