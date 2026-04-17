def f(n, m):
    if n == m: return 1
    if n > m or n == 40: return 0
    return f(n+2, m) + f(n +3 , m) + f(n*2, m)

print(f(17, 35) * f(35, 73))