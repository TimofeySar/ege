from math import *

for l in range(1, 1000):
    alf = ceil(log2(l))
    b = 252500 * 261 * alf
    if b > 31 * 1024*1024*8:
        print(l)
        break

