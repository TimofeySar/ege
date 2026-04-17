def f(s, m):
    if s <= 16: return m%2 == 0
    elif m ==0:
        return 0
    h = [f(s - 3, m-1), f(s-8, m-1), f(int(s/3), m-1)]
    if m %2 != 0:
        return (any(h))
    else:
        return all(h)

print('19', [s for s in range(1000, 16,-1) if not(f(s,1)) and f(s, 2)])
print('20', [s for s in range(1000, 16,-1) if not(f(s,1)) and f(s, 3)])
print('20', [s for s in range(1000, 16,-1) if not(f(s,2)) and f(s, 4)])