# # for i in range(1, 100000000000000000):
# #     s = 0
# #     for k in range(1, i + 1):
# #         if i % k == 0:
# #             s = s + 1
# #     if s <= 2:
# #         print(i)
# def F(n):
#     if n == 1:
#         return 1
#     if n > 1:
#         return 2 * F(n-1) + 1
# print(F(5))
#
#
#
#

from functools import *
import sys
sys.setrecursionlimit(10000000)

@lru_cache(None)
def f(n):
    return g(n-1)

@lru_cache(None)
def g(n):
    if n <=9: return 3*n
    return g(n-2)+1
for n in range(50000):
    f(n)
print(f(47995))