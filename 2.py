# from itertools import product
# print("x y z w")
# def f(x, y, z, w):
#     if (y <= (not(x <= z))) or w:
#         return True
#     return False
#
# for x, y, z, w in product([0, 1], repeat=4):
#     if f(x, y, z, w) == 0:
#         print(x, y, z, w)
#
#
# print("x y z w")
# for x in range(0, 2):
#     for y in range(0, 2):
#         for z in range(0, 2):
#             for w in range(0, 2):
#                 if ((not(y)) <= (z == w)) and ((z <= x) == w):
#                     print(x, y, z, w)
from itertools import product
print('x y z w')
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if ((not x) and z and (not y) and (not w)) or ((not x) and z and y and (not w)) or ((not x) and z and y and w):
                    print(x,y,z,w)
#105
#xywz
#420
#19
# 49
# 6 101084
# 7 405106
# 8 - 9295
# 9 823
#10 74
#11 - 32768
#12 - 1929
#13 - 743
#14 - 24
# 15 - 30