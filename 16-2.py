from functools import lru_cache


@lru_cache
def f(n):
    if n >= 2024:
        return 1
    else:
        return f(n + 2) + f(n + 4)


a = set()
for i in range(2025, 0, -1):
    a.add(f(i))
print(len(a))
