def f(s,m):
    if s >= 41:
        return m%2 == 0
    elif m == 0:
        return 0
    if s*2 <=50:
        h = [f(s+1, m-1), f(s+2, m-1), f(s*2, m-1)]
    elif s+2 <=50 :
        h = [f(s+1, m-1), f(s+2, m-1)]
    elif s+1 <=50 :
        h = [f(s+1, m-1)]
    else:
        return 0
    if m %2 !=0:
        return all(h)
    return any(h)

print([s for s in range(1, 40) if not(f(s, 1)) and f(s, 3)])