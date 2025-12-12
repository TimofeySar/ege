from itertools import product

for x, y, z, w in product([0,1], repeat=4):
    if ((not x) or y) and (z <= x) and not(w):
        print(x,y,z,w)