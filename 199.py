def f(s, m):
    if s >= 42:
        return m%2 ==0
    elif m ==0:
        return 0

    h = [f(s+1, m-1), f(s+3, m-1), f(s*2, m-1)]
    if m%2 != 0:
        return any(h)
    return any(h)

print('19', [s for s in range(1, 41) if not f(s,1) and f(s, 2)])

