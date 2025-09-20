from itertools import product
print("x y z w")
def f(x, y, z, w):
    if (y <= (not(x <= z))) or w:
        return True
    return False

for x, y, z, w in product([0, 1], repeat=4):
    if f(x, y, z, w) == 0:
        print(x, y, z, w)