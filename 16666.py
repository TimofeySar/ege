from functools import lru_cache


@lru_cache(maxsize=None)
def f(n):
    if n <10:
        return 3
    else:
        return (n+4) * f(n-5)

for i in range(2, 257490, 5):
    f(i)
print((f(257487)//683 + f(257477)// 67) // f(257472))