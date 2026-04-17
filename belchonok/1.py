from math import *

def dell(n):
    m = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            m.append(i)
            m.append(n//i)
    return sorted(list(set(m)))


for i in range(1300000000, 1800000001):
    a = dell(i)
    if prod(a) %57 == 0:
        print(i)
        break
