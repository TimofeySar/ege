def f(s, m):
    if s>= 103: return m%2==0

    elif m == 0:
        return 0
    h = []
    if (s + 1) % 3 != 0: h.append(f(s + 1, m - 1))
    if (s + 2) % 3 != 0: h.append(f(s + 2, m - 1))
    if (s * 2) % 3 != 0: h.append(f(s * 2, m - 1))
    if m%2!=0:
        return any(h)
    return all(h)

print([s for s in range(1, 101) if s % 3 != 0 and not(f(s, 2)) and f(s, 4)])