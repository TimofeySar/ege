from functools import lru_cache

@lru_cache(None)
def f(n):
    if n ==1:
        return 1
    else:
        return (n+1)*f(n-1)

for i in range(1, 2026):
    f(i)
print(((f(2025)//2026) + f(2024))//f(2023))