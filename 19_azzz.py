def f(s,m):
    if s >= 73:
        return m%2==0
    elif m<=0:
        return 0
    if s %2 == 0:
        h = [f(s + 4, m - 1), f(s * 3, m-1)]
    elif s%2 !=0:
        h = [f(s +4, m - 1), f(s * 2, m - 1)]
    if (m-1)%2 == 0:
        return any(h)
    else:
        return all(h)

print([s for s in range(1, 73) if not(f(s, 2)) and f(s,4)])
