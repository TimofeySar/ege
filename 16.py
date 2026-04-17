# for i in range(1, 100000000000000000):
#     s = 0
#     for k in range(1, i + 1):
#         if i % k == 0:
#             s = s + 1
#     if s <= 2:
#         print(i)

from functools import lru_cache

@lru_cache(maxsize=None)
def f(n):
    if n >= 2025:
        return n
    elif n < 2025:
        return n + 3 + f(n + 3)


for i in range(2026, 10, -1):
    f(i)
print(f(23) - f(21))