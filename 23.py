# def f(x, y):
#     if x >y or x == 15:
#         return 0
#     if x == y:
#         return 1
#     return f(x+2, y) + f(x+5, y) + f(x * 3, y)
# print(f(1, 10) *f(10,31))
# from functools import lru_cache
#
# @lru_cache(None)
# def f(x,y,z):
#     if x>y or '6' in str(x) or z > 50:
#         return 0
#     elif x == y:
#         return 1
#     else:
#         return f(x + 1, y, z+1) + f(x + 5,y,z+1)+ f(x*2 ,y,z+1)
# print(f(0, 312025, 0))

from functools import lru_cache
@lru_cache(None)
def f(x,y,z):